"""riskdash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from riskdashapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^riskdashapp/', include('riskdashapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^controls/', views.controls, name='controls'), 
    url(r'^risks/', views.risks, name='risks'),
    url(r'^summary/', views.summary, name='summary'),
    url(r'^topten/', views.topten, name='topten'),
]

