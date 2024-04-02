from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.home, name='my_home'),
    path('service/', views.service, name='service'),
    path('featured_cars/', views.featured_cars, name='featured-cars'),
    path('new_cars/', views.new_cars, name='new-cars'),
    path('brand/', views.brand, name='brands'),
    path('contact/', views.contact, name='contact'),
    path('client_say/', views.client_say, name='client_say'),

]


