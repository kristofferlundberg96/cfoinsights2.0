from django.core.management.base import BaseCommand, CommandError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Generates an API key for a user with a given username.'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+', type=str)

    def handle(self, *args, **options):
        for username in options['username']:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            token = Token.objects.create(user=user)

            self.stdout.write(self.style.SUCCESS('Successfully generated API key "%s"' % token))
