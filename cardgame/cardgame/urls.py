"""cardgame URL Configuration

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
from registration import views as v
from feed import views as v_feed
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('registration/logout_done/', v.logout_done, name="logout_done"),
    path('registration/login_done/', v.login_done, name="login_done"),
    path('feed/<int:id>', v_feed.feed, name="feed"),
    path('feed/<str:name>', v_feed.blog_open, name="blog"),

]
