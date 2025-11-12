from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from relationship_app.models import Book
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Setup initial groups and permissions'

    def handle(self, *args, **options):
        book_ct = ContentType.objects.get_for_model(Book)

        can_view = Permission.objects.get(codename='can_view', content_type=book_ct)
        can_create = Permission.objects.get(codename='can_create', content_type=book_ct)
        can_edit = Permission.objects.get(codename='can_edit', content_type=book_ct)
        can_delete = Permission.objects.get(codename='can_delete', content_type=book_ct)

        viewers, _ = Group.objects.get_or_create(name='Viewers')
        editors, _ = Group.objects.get_or_create(name='Editors')
        admins, _ = Group.objects.get_or_create(name='Admins')

       
        viewers.permissions.set([can_view])
        editors.permissions.set([can_view, can_create, can_edit])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully!"))
