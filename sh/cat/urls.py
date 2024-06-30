from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_page, name='home'),
    path('thanks/', views.thanks, name='thanks'),
    path('stabilizer/', views.stabilizer_page, name='stabilizer'),
    path('power-asic/', views.power_asic, name='power_asic'),
    path('stabilizer/one-phase/', views.stabilizer_one_phase, name='stabilizer_one_phase'),
    path('stabilizer/three-phase/', views.stabilizer_three_phase, name='stabilizer_three_phase'),
    path('stabilizer/stabilizer-low-price/', views.stabilizer_low_price, name='stabilizer_low_price'),
    path('stabilizer/stabilizer-max-price/', views.stabilizer_max_price, name='stabilizer_max_price'),
    path('favourite/', views.favorites_page, name='favourite_page'),
    path('<slug:slug>/', views.asic_detail, name='asic_detail'),
    path('stabilizer/<slug:slug>/', views.stabilizer_detail, name='stabilizer_detail'),
    path('brand/<slug:slug>/', views.brand_detail, name='brand_slug'),
    path('stabilizer/stabilizer_brand/<slug:slug>/', views.stabilizer_brand_detail, name='stabilizer_brand'),
    path('fil/<slug:slug>/', views.brand_detail, name='fil_slug'),
    path('asic-added/<slug:slug>/', views.add_to_favorites, name='add_asic'),
]
