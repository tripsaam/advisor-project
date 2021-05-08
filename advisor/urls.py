"""advisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from posts import views
from userinterface.views import RegisterAPI, LoginAPI
from knox import views as knox_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('advisor/', views.PostList.as_view()),
    path('user/<int:pk>/advisor', views.PostList.as_view()),
    path('user/register/', RegisterAPI.as_view(), name='register'),
    path('user/login/', LoginAPI.as_view(), name='login'),
    # path('user/<username>/advisor/', PostList.as_view()),
    # path('user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('user/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
