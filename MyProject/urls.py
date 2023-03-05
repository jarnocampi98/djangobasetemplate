"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# File per la registrazione dell rotte di primo livello
# Qui vengono registrate tutte le rotte per le altre app, la rotto per l'admin-interface e la rotta per i media

from django.contrib import admin
from django.urls import path, include

from django.conf import settings # setting mi permette di utilizzare le costanti definite nel file settings.py della cartella di progetto
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
    path('app1/', include('app1.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # appendo alla lista le rotte per tutti i media (collocati nella cartella /media)
    
