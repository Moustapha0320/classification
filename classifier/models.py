from django.db import models
from django.conf import settings

class ImagePrediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Correction ici
    image = models.ImageField(upload_to='prediction/')
    predicted_class = models.CharField(max_length=50)
    confidence = models.FloatField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_class} ({self.confidence}%)"

