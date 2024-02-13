from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "guns"
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:gun_id>', views.detail, name="detail")
]