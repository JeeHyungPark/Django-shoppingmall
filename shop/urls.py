from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', product_in_category, name='product_all'), #전체제품 노출
    path('<slug:category_slug>/', product_in_category, name='product_in_category'), #카테고리 선택
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'), #제품 상세
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
