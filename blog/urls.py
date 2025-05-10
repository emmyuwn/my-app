from django.contrib import admin
from django.urls import path
from . import views
from .views import product_list

from .views import create_payment
 # Import the views file from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu_view, name='menu'),
      path('', views.home, name='home'),  # Add a path for the HTML page
     path('contact/', views.contact, name='contact'),
     path('search/', views.search, name='search'), 
    path('about/', views.about, name='about'),  
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', product_list, name='product_list'),
    path("pay/", create_payment, name="pay"),
]






    


