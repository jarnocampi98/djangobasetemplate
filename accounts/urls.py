
# File per la registrazione dell rotte dell'app accounts

from django.urls import path
from .views import registrazione_view

urlpatterns = [
    path('registrazione/', registrazione_view, name="registrazione_view"), 
]