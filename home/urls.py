from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about us'),
    path('contact/', views.contact, name='contact us'),
    path('product/<cat_id>', views.product),
]