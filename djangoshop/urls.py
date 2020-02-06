from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')), #cart/urls.py 연결하기
    path('coupon/', include('coupon.urls')),
    path('', include('shop.urls')), #shop/urls.py 연결하기
    
]

