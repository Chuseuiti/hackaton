"""blochack_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from information import views as view_inf
from registration import views as view_reg

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', view_reg.register, name = 'register'),
    url(r'^authentication/', view_reg.authentication, name = 'authentication'),
    url(r'^information/', view_inf.information_request, name = 'information_request'),
    url(r'^document/raw/', view_inf.document_raw, name = 'document_raw'),
    url(r'^document/encrypt/', view_inf.document_encrypt, name = 'document_encrypt')
]
