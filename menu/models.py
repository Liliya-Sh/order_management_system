from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории товаров"""
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=Menu.Status.AVAILABILITY)


class Menu(models.Model):
    """Товары пиццерии"""
    class Status(models.IntegerChoices):
        ABSENT = 0, 'Отсутствует'
        AVAILABILITY = 1, 'Вналичие'

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product', verbose_name='Категория')
    name_product = models.CharField(max_length=200, verbose_name='Наименование блюда')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(max_length=500, null=True, verbose_name='Состав')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    is_available = models.BooleanField(choices=Status.choices, default=Status.AVAILABILITY, verbose_name='Наличие')
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, default='Добавить изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления в меню')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ('name_product',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name_product

    def get_absolute_url(self):
        return reverse('menu:product_detail',  args=[self.slug])
