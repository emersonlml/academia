from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import CITeacher
from accounts.models import Profile  # Asegúrate de importar el modelo Profile correctamente

class Command(BaseCommand):
    help = 'Poblar la tabla CITeacher con los datos de los profesores'

    def handle(self, *args, **kwargs):
        # Obtener los usuarios que pertenecen al grupo "profesores"
        profesores = User.objects.filter(groups__name='profesores')

        for profesor in profesores:
            # Obtener el perfil asociado al profesor
            try:
                profile = profesor.profile
            except Profile.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'El usuario {profesor.username} no tiene un perfil.'))
                continue

            # Crear o actualizar el registro en CITeacher
            teacher_data, created = CITeacher.objects.get_or_create(
                user=profesor,
                defaults={
                    'first_name': profesor.first_name,
                    'last_name': profesor.last_name,
                    'ci': profile.telephone  # Tomar el teléfono como el CI
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Se ha creado el registro para {profesor.username}.'))
            else:
                self.stdout.write(self.style.WARNING(f'El registro para {profesor.username} ya existe.'))
