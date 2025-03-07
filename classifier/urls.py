from django.urls import path
from .views import index, dashboard
from .views import generate_adversarial, download_file

urlpatterns = [
    path("index/", index, name="index"),  # Page pour analyser une image
    path("dashboard/", dashboard, name="dashboard"),  # Dashboard après connexion
    path('generate_adversarial/', generate_adversarial, name='generate_adversarial'),
    path("classifier/download/<str:filename>/", download_file, name="download_file"),
]
