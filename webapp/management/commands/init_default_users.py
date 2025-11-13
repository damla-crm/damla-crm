from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create default users: ramazan and damla with password 123456"

    def handle(self, *args, **options):
        for username in ["ramazan", "damla"]:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"is_staff": True}
            )
            user.set_password("123456")
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"User {username}: {'created' if created else 'updated'}"))
        self.stdout.write(self.style.SUCCESS("Default users initialized."))
