import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('data.json') as file:
            data_to_create = json.load(file)

        cat_to_create = []

        for i, data in enumerate(data_to_create[:5]):
            cat_to_create.append(Category(**data['fields'], pk=i+1))

        Category.objects.bulk_create(cat_to_create)

        for i, data in enumerate(data_to_create[5:]):
            Product.objects.create(pk=i+1,
                                   name=data['fields']['name'],
                                   description=data['fields']['description'],
                                   photo=data['fields']['photo'],
                                   category=Category.objects.get(pk=data['fields']['category'] % 10),
                                   price=data['fields']['price'])
