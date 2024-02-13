from . import views
from django.contrib import admin
from django.urls import include, path

app_name = "attendance"
urlpatterns = [
    path('', views.subject_list, name="subject_list"),
    path('report/<int:subject_id>', views.subject_report, name="report"),
    path('add/', views.add_subject, name="add"),
    path('edit/<int:subject_id>', views.edit_subject, name="edit"),
    path('delete/<int:subject_id>', views.delete_subject, name="delete"),
]