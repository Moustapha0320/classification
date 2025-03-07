from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
import uuid
from users.models import UserAccount

# Inscription
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect("register")

        if UserAccount.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            return redirect("register")

        user = UserAccount.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Compte créé avec succès ! Connectez-vous.")
        return redirect("login")

    return render(request, "users/register.html")

# Connexion
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token = str(uuid.uuid4())
            request.session["auth_token"] = token
            request.session["username"] = user.username
            return redirect("dashboard")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect("login")

    return render(request, "users/login.html")

# Déconnexion
def user_logout(request):
    request.session.pop("auth_token", None)
    request.session.flush()
    return redirect("login")
