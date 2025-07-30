import time
from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db...")
        time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
