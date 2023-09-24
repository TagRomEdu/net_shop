import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Category.objects.all().delete()

        with open('data.json') as file:
            data_to_create = json.load(file)

        cat_to_create = []
        for data in data_to_create:
            cat_to_create.append(Category(**data['fields']))

        Category.objects.bulk_create(cat_to_create)
