from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mark,Registration
from .models import CITeacher  # Importa el modelo CITeacher
from accounts.models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=Registration)
def create_marks(sender, instance, created, **kwargs):
    if created:
        materias = instance.course.materias.all()
        for materia in materias:
            Mark.objects.create(
            materia=materia,
           # matera=instance.materia,
            student=instance.student,
            mark_1=None,
            mark_2=None,
            mark_3=None,
            average=None
            )
        
@receiver(post_save, sender=User)
def create_or_update_citeacher(sender, instance, created, **kwargs):
    # Verifica si el usuario pertenece al grupo 'profesores'
    if instance.groups.filter(name='profesores').exists():
        # Verifica si el usuario tiene un perfil y si el campo 'telephone' no está vacío
        if hasattr(instance, 'profile') and instance.profile.telephone:
            ci = instance.profile.telephone  # El CI está en el campo telephone
            
            # Si es un nuevo usuario, creamos el registro en CITeacher
            if created:
                CITeacher.objects.create(
                    user=instance,
                    first_name=instance.first_name,
                    last_name=instance.last_name,
                    ci=ci
                )
            else:
                # Si el usuario ya existe, obtenemos o creamos el registro de CITeacher
                citeacher, created = CITeacher.objects.get_or_create(user=instance)
                citeacher.first_name = instance.first_name
                
                citeacher.last_name = instance.last_name
                citeacher.ci = ci
                citeacher.save()
        else:
            print(f"El usuarioo {instance.username} no tiene un perfil o su teléfono no está establecido.")
#python manage.py populate_citeachers
