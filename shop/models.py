from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.CASCADE, null=True, verbose_name='производитель')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    discount = models.BooleanField(default=False, verbose_name='со скидкой')
    sale = models.DecimalField(default=1, decimal_places=2, max_digits=3)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class Image(models.Model):
    img = models.ImageField(upload_to='product/%Y/%m/%d')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_image')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class Rating(models.Model):
    rating  = models.PositiveIntegerField()
    review = models.CharField(max_length=300, verbose_name='Отзыв', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rating')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = ('user', 'product')


