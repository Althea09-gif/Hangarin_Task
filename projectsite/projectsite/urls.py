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
from django.urls import path
from Hangarin.views import dashboard, task_detail, create_task, edit_task, delete_task

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("tasks/new/", create_task, name="create_task"),
    path("tasks/<int:task_id>/", task_detail, name="task_detail"),
    path("tasks/<int:task_id>/edit/", edit_task, name="edit_task"),
    path("tasks/<int:task_id>/delete/", delete_task, name="delete_task"),
]