from django.core.management.base import BaseCommand, CommandError

from shortner.models import UrlprojectURL


class Command(BaseCommand):
    help = 'refreshes all UrlprojectURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return UrlprojectURL.objects.refresh_shortcodes(items=options['items'])