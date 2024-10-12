import os
import sys

# Add the absolute path to 'djangoapp' to sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'djangoapp'))

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forecast_solar.settings')

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    execute_from_command_line(sys.argv)