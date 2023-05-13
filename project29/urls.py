"""project29 URL Configuration

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('cbv_string/',cbv_string.as_view(),name='cbv_string'),
    path('fbv_html/',fbv_html,name='fbv_html'),
    path('cbv_html/',cbv_html.as_view(),name='cbv_html'),
    path('fbf_form/',fbf_form,name='fbf_form'),
    path('cbf_form/',cbf_form.as_view(),name='cbf_form'),
    path('CBV_direct/',TemplateView.as_view(template_name='CBV_direct.html'),name='CBV_direct')
    
    
]
