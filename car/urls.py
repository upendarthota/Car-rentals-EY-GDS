from django.contrib import admin
from django.urls import include,path
from car import views

urlpatterns = [
    path('',views.inde,name="inde"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/',views.home,name="home"),
    path('cars/',views.cars,name="cars"),
    path('contact/',views.contact,name="contact"),
    path('rent/<int:car_id>',views.rent,name="rent"),
    path('rented/',views.Rent,name="Rent"),
    path('payment/',views.payment,name="payment"),
    path('about/',views.about,name="about"),
    path('payconf/',views.payconf,name="payconf"),
    path('profile/',views.profile,name="profile"),
    path('serve/',views.serve,name="serve"),
    
    
    
    
]