import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.management import execute_from_command_line
execute_from_command_line(["manage.py", "runserver"])
