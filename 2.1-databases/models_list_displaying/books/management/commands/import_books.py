from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        book1 = Book(name="Три мушкетера", author="Дюма", pub_date="1782-01-12").save()
        book2 = Book(name="Spider-Man", author="J.Rich", pub_date="1984-06-05").save()
        book3 = Book(name="Как не сойти с ума от Python", author="Лутц", pub_date="2004-03-01").save()
