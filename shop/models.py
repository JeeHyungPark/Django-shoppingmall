from django.db import models
from django.urls import reverse

class Category(models.Model): #제품 카테고리 모델
    name = models.CharField(max_length=200, db_index=True) #카테고리이름을 db에서 index값으로 설정
    meta_description = models.TextField(blank=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    #slug => 글번호를 이용하는 것이 아닌, 상품명 등을 이용해서 url을 만드는 방식

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): #객체 추가/수정에 대한 기본 반환주소를 반환
        return reverse('shop:product_in_category', args=[self.slug])
        #reverse함수 => 되돌아갈 페이지의 패턴 이름이 shop app의 product_in_category,
        #args => 여러 값들을 리스트로 전달하는데 사용(url을 만드는데에 필요한 pk)

class Product(models.Model): #제품 모델
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    # ForeignKey를 사용하여 카테고리 모델과 관계를 만듬, 카테고리가 삭제되어도 상품은 남아있기 위해 on_delete=SET_NULL
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='../products/%Y/%m/%d', blank=True) #image에 빈칸 허용하는거 아닌가? 왜 사진 안넣으면 메인페이지 에러 나지 ㅠ
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id','slug']] #멀티 컬럼 색인 기능 / id와 slug 필드를 묶어서 색인이 가능하도록

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
