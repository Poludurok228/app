from django.urls import path
from . import views

app_name = 'telegram'

urlpatterns = [
    path('', views.index, name='home'),
    path('brand_cat/', views.brand_cat, name='brand_cat'),
    path('brand_cat/<slug:slug>/', views.brand_detail, name='brand_detail_t'),
    path('basket/', views.basket_page, name='basket'),
    path('add_to_basket/<int:asic_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove_single_from_basket/<int:asic_id>/', views.remove_single_from_basket, name='remove_single_from_basket'),
    path('remove_all_from_basket/<int:asic_id>/', views.remove_all_from_basket, name='remove_all_from_basket'),
    path('pay/', views.pay, name='pay'),
    path('choice-network/', views.choice_network, name='choice_network'),
    path('wallet-usdt/<slug:slug>/', views.net_detail, name='wallet_usdt'),
    path('help_page/', views.solo_page, name='solo_page'),
]
