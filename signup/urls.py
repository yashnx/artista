from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin , name="signin"),
    path('api/', views.api , name="api"),
    path('loggedin/', views.loggedin , name="loggedin"),
    path('loggedout/', views.loggedout , name="loggedout"),
    path('search/', views.search, name="search"),
    path('filter/', views.filter, name="filter"),
    
]