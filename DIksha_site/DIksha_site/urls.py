"""DIksha_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

#code for video 6 in with hello word is show in page
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('about', views.about, name='about')
# ]

#code for video 7 designing pipes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Analyze', views.Analyze, name='Analyze'),
    # path('Capitalizefirst', views.Capitalizefirst, name='capital'),
    # path('Newlineremove', views.Newlineremove, name='Newlineremov'),
    # path('Spaceremover', views.Spaceremover, name='Spaceremover'),
    # path('Charcount', views.Charcount, name='Charcount'),
]