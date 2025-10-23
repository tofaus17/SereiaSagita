import os
import webbrowser
import time
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SereiaSagita.settings")

def run():
    webbrowser.open("http://127.0.0.1:8000")
    execute_from_command_line(["manage.py", "runserver", "--noreload"])

if __name__ == "__main__":
    run()
