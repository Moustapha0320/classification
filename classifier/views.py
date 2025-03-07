import os
import numpy as np
from django.conf import settings
from tensorboard.compat import tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from image_classifier.settings import UPLOAD_FOLDER
from .models import ImagePrediction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse

# Charger le modèle IA
MODEL_PATH = os.path.join(settings.BASE_DIR, "classifier/model/saved_model.h5")
model = load_model(MODEL_PATH)
CLASSES = ["Moto", "voiture", "Bâteau"]

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Fonction de prédiction
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)
    predicted_class = CLASSES[np.argmax(predictions)]
    confidence = round(100 * np.max(predictions), 2)
    return predicted_class, confidence

# Page d'accueil

@login_required  # Assure que seul un utilisateur connecté peut accéder
def index(request):
    print("Session avant POST :", request.session.items())

    if request.method == "POST" and request.FILES.get("file"):
        image_file = request.FILES["file"]
        image_path = os.path.join(settings.MEDIA_ROOT, "prediction", image_file.name)

        with open(image_path, "wb+") as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        predicted_class, confidence = predict_image(image_path)

        # ✅ Sauvegarde de la prédiction associée à l'utilisateur actuel
        prediction = ImagePrediction(
            user=request.user,  # Associe la prédiction à l'utilisateur connecté
            image=f"prediction/{image_file.name}",
            predicted_class=predicted_class,
            confidence=confidence
        )
        prediction.save()

        request.session.modified = True
        print("Session après POST :", request.session.items())

        return render(request, "classifier/result.html", {
            "image_path": f"{settings.MEDIA_URL}prediction/{image_file.name}",
            "predicted_class": predicted_class,
            "confidence": confidence
        })

    return render(request, "classifier/index.html")


# Dashboard (historique des prédictions)
@login_required
def dashboard(request):
    token = request.session.get("auth_token")

    if not token:
        return redirect("login")

    predictions = ImagePrediction.objects.filter(user=request.user).order_by('-uploaded_at')  # Charge uniquement les prédictions de l'utilisateur connecté
    return render(request, "classifier/dashboard.html", {"predictions": predictions})
    response = render(request, "classifier/dashboard.html", {"predictions": predictions})
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"

    return response

def generate_adversarial_example(model, original_image, epsilon=0.2):
    """
    Génère une image adversariale en ajoutant du bruit contrôlé à l'image originale.
    """
    perturbation = tf.random.uniform(original_image.shape, -epsilon, epsilon)
    adversarial_image = original_image + perturbation
    adversarial_image = tf.clip_by_value(adversarial_image, -1, 1)
    return perturbation, adversarial_image

def save_adversarial_image(adversarial_image, save_path):
    """
    Sauvegarde l'image adversariale générée.
    """
    adversarial_image = (adversarial_image.numpy()[0] + 1) / 2.0 * 255.0  # Normalisation inverse
    adversarial_image = np.clip(adversarial_image, 0, 255).astype(np.uint8)
    tf.keras.preprocessing.image.save_img(save_path, adversarial_image)

@login_required
def generate_adversarial(request):
    """
    Vue Django pour générer une image adversariale en fonction de l'epsilon sélectionné.
    """
    if request.method == "POST":
        if 'file' not in request.FILES:
            return render(request, 'classifier/generate_adversarial.html', {"error": "Aucun fichier n'a été envoyé."})

        file = request.FILES['file']
        if file.name == '':
            return render(request, 'classifier/generate_adversarial.html', {"error": "Aucun fichier sélectionné."})

        # Récupérer l'epsilon sélectionné par l'utilisateur
        epsilon = float(request.POST.get("epsilon_selection", 0.1))  # Valeur par défaut = 0.1

        filepath = os.path.join(UPLOAD_FOLDER, file.name)

        with open(filepath, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        try:
            # Charger l'image et la prétraiter
            img = tf.keras.preprocessing.image.load_img(filepath, target_size=(224, 224))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
            original_image = np.expand_dims(img_array, axis=0)

            # Générer l'image adversariale avec l'epsilon sélectionné
            perturbation, adversarial_image = generate_adversarial_example(model, original_image, epsilon)

            # Sauvegarde de l'image adversariale
            adv_filename = f"adversarial_{file.name}"
            adv_save_path = os.path.join(UPLOAD_FOLDER, adv_filename)
            save_adversarial_image(adversarial_image, adv_save_path)

            return render(request, 'classifier/generate_adversarial.html', {
                "adv_image_path": f"{settings.MEDIA_URL}uploads/{adv_filename}",
                "image_path": f"{settings.MEDIA_URL}uploads/{file.name}",
                "adv_save_path": adv_filename
            })
        except Exception as e:
            return render(request, 'classifier/generate_adversarial.html', {"error": f"Erreur : {str(e)}"})


    return render(request, 'classifier/generate_adversarial.html')

@login_required
def download_file(request, filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    return HttpResponse("Fichier non trouvé.", status=404)
