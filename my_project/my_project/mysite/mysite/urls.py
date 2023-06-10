"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path
from pools.controllers import index
from pools.controllers import feedback
from pools.controllers import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.index),
    path('about/', index.about),
    path('contacts/', index.contacts),
    path('hobbies/', index.hobbies),
    path('gallery/', index.gallery),
    path('photo/', index.photo),
    path('feedback/', feedback.create),
    path('feedback/index', feedback.index),
    path('opros.html', index.opros),
    path('calc.html', index.calc),
    path('logo.html', index.logo),
]
