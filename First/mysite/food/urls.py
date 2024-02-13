from . import views
from django.urls import include, path

app_name = 'food' # For namespacing the urls
urlpatterns = [
    path('', views.home, name="home"),
    # path('', views.HomeClassView.as_view(), name="home"),
    path('<int:item_id>/', views.detail, name="detail"),
    # path('<int:pk>/', views.DetailClassView.as_view(), name="detail"),
    path('add/', views.add_item, name="add_item"),
    # path('add/', views.CreateItem.as_view(), name="add_item"),
    path('update/<int:item_id>/', views.update_item, name="update_item"),
    path('delete/<int:item_id>/', views.delete_item, name="delete_item"),
    path('deleteform/', views.delete_select, name="delete_form"),
    path('search/', views.search, name="search"),
]