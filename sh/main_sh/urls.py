from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/', views.blog_page, name='blog'),
    path('contact/', views.map_page, name='contact'),
    path('placement/', views.placement, name='placement'),
    path('about/', views.about_us, name='about'),
    path('blog/<slug:slug>/', views.detail_news, name='detail_news'),
    path('blog/news-by-tags/<slug:slug>/', views.detail_tags, name='detail_tag'),
    path('check-order/', views.check_order, name='check_order'),
    path('check-warranty/', views.check_warranty, name='check_warranty'),
    path('download-price-list/', views.download_file, name='download_price_list'),
    path('contracts/regulation-on-personal-data/', views.contracts, name='contract1'),
    path('contracts/privacy-policy/', views.contract_2, name='contract2'),
    path('contracts/the-offer-agreement/', views.contract_3, name='contract3'),
    path('contracts/delivery-and-pay/', views.contract_4, name='contract4'),
    path('sorry/', views.sorry, name='sorry'),
]
