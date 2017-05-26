from django.core.management.base import BaseCommand, CommandError
from validate.models import Code
import random

def get_no():
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(a) for i in range(25))


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('num', nargs='?', type=int)

    def handle(self, *args, **options):
        num = options['num']
        for i in range(num):
            code = get_no()
            Code.objects.create(code=code)
            print(code)
        #for num in options['num']:
            #try:
                #poll = Poll.objects.get(pk=poll_id)
            #except Poll.DoesNotExist:
                #raise CommandError('Poll "%s" does not exist' % poll_id)

            #poll.opened = False
            #poll.save()

            #self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))