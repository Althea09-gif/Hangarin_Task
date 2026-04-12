"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from Hangarin.views import (
    dashboard,
    home,
    task_detail,
    create_task,
    edit_task,
    delete_task,
    signup_view,
    profile_view,
    settings_view,
)
from Hangarin.forms import LoginForm

urlpatterns = [
    path("admin/", admin.site.urls),

    # PWA routes
    path("", include("pwa.urls")),

    # Main pages
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("signup/", signup_view, name="signup"),
    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=LoginForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

    # User pages
    path("profile/", profile_view, name="profile"),
    path("settings/", settings_view, name="settings"),

    # Task pages
    path("tasks/new/", create_task, name="create_task"),
    path("tasks/<int:task_id>/", task_detail, name="task_detail"),
    path("tasks/<int:task_id>/edit/", edit_task, name="edit_task"),
    path("tasks/<int:task_id>/delete/", delete_task, name="delete_task"),
]