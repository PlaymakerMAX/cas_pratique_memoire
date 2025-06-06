# config_projet_devsecops/urls.py
from django.contrib import admin
from django.urls import path, include # Ajoute 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist_app.urls')), # Ajoute cette ligne pour inclure les URLs de notre app
]