import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand  
from django.core.management import call_command  
  
class Command(BaseCommand):  
    help = 'Initialize the app by running multiple management commands'  
  
    def handle(self, *args, **options):  
        # Run the 'redis --start' command  
        self.stdout.write(self.style.WARNING('Starting Redis...'))  
        os.system('redis-server --daemonize yes')  
        self.stdout.write(self.style.SUCCESS('Redis started'))  
  
        # Run the 'rabbitmq --start' command  
        self.stdout.write(self.style.WARNING('Starting RabbitMQ...'))  
        os.system('rabbitmq-server start -detached')  
        self.stdout.write(self.style.SUCCESS('RabbitMQ started'))  
  
        # Run the 'celery --start' command  
        self.stdout.write(self.style.WARNING('Starting Celery...'))  
        os.system('sudo mkdir -p /var/run/celery; sudo chmod 777 /var/run/celery')
        os.system('sudo mkdir -p /var/log/celery; sudo chmod 777 /var/log/celery')
        os.system('celery multi start w1 -A chirps -l INFO')
        self.stdout.write(self.style.SUCCESS('Celery started'))  
  
        # Run the 'makemigrations' command  
        self.stdout.write(self.style.WARNING('Running makemigrations...'))  
        call_command('makemigrations')  
        self.stdout.write(self.style.SUCCESS('makemigrations completed'))  
  
        # Run the 'migrate' command  
        self.stdout.write(self.style.WARNING('Running migrate...'))  
        call_command('migrate')  
        self.stdout.write(self.style.SUCCESS('migrate completed'))  
  
        # Check if a superuser already exists  
        if not User.objects.filter(is_superuser=True).exists():  
            # Run the 'createsuperuser' command  
            self.stdout.write(self.style.WARNING('Creating superuser...'))  
            call_command('createsuperuser')  
            self.stdout.write(self.style.SUCCESS('Superuser created'))  
        else:  
            self.stdout.write(self.style.WARNING('Superuser already exists. Skipping superuser creation.'))  
  
        # Run the 'loaddata' command  
        self.stdout.write(self.style.WARNING('Loading data from fixtures...'))  
        call_command('loaddata', 'plan/fixtures/plan/employee.json')  
        self.stdout.write(self.style.SUCCESS('Data loaded from fixtures'))  
  
        # Run the 'runserver' command  
        self.stdout.write(self.style.WARNING('Starting the development server...'))  
        call_command('runserver')  
        self.stdout.write(self.style.SUCCESS('Development server started'))  
  
        self.stdout.write(self.style.SUCCESS('App initialization completed'))  
