import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели

            # Решение 1

            # Phone.objects.create(
            #     id=phone["id"],
            #     name=phone["name"],
            #     price=phone["price"],
            #     image=phone["image"],
            #     release_date=phone["release_date"],
            #     lte_exists=phone["lte_exists"],
            #     slug=slugify(phone["name"]),
            # )

            # Решение 2

            Phone.objects.create(
                phoneModel=slugify(phone["name"]),
                **phone
            )
