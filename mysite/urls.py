"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

# Cambiar la URL de "Ver sitio" en el admin
admin.site.site_url = '/blog/'  # Ahora "Ver sitio" redirige al blog

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/admin/')),  # Redirige la raíz al admin
    path('admin/', admin.site.urls),  # URL del panel de administración
    path('blog/', include('blog.urls')),  # URLs del blog
]
