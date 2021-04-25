import os
import csv
from core.models import GhostName
from django.core.management.base import BaseCommand
from django.conf import settings

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Commands:
# ----------------------------------------------- #
class Command(BaseCommand):
    help = "Populates ghost names with from the ghost_names csv"

    def handle(self, *args, **options):
        added_names = 0
        print('Adding ghosts names from local csv')
        file_location = os.path.join(
            settings.BASE_DIR, "core", "gosht_data", "ghost_names.csv")
        with open(file_location, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                name, description = row
                if not GhostName.objects.filter(name=name).first():
                    new_ghost = GhostName.objects.create(
                        name=name, description=description
                    )
                    new_ghost.save()
                    added_names += 1

        print("Added names:{}".format(added_names))
