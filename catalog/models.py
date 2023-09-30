from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('id',)


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена")
    creating_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"Категория: {self.category}\nНаименование: {self.name}, стоимость: {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.CharField(max_length=250, **NULLABLE, verbose_name="slug")
    text = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='media/', **NULLABLE, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Признак публикации")
    view_count = models.IntegerField(verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.name}, {self.slug}, views: {self.view_count}'

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
