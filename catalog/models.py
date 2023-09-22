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


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.IntegerField()
    creating_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return f"Категория: {self.category}\nНаименование: {self.name}, стоимость: {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
