from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
import PIL as pillow

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Наименование категории')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Количество комнат в квартире'
        verbose_name_plural = 'Количество комнат в квартирах'

class Product(models.Model):

    name = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Наименование')
    # price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    # discount = models.IntegerField(default=0)# поле для скидки
    # price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name='Категория квартиры')
    short_description = models.TextField(max_length=50, blank=True, null=True, default=None, verbose_name='Кр. описание')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Полное описание')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')


    def description_S(self):
        return truncatechars(self.description, 30)
    def __str__(self):
            return "%s" % (self.name)


    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

class ProductImage(models.Model):
    Product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Квартира')
    image = models.ImageField(upload_to='products_images/', verbose_name='Фотография')
    is_main = models.BooleanField(default=False, verbose_name='Главная')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')
    def __str__(self):
            return "%s" % (self.id)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'