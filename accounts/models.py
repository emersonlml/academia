"""
Autor: Emerson ibañez
Fecha: 2025-01-30
Descripción: 
"""
"""
Autor: Emerson Ibañez
Fecha: 30
Proyecto: Sistema de Control Académico
Descripción:  ADV 2025
"""


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# PERFIL DE USUARIO
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='default.png', upload_to='users/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')
    create_by_admin = models.BooleanField(default=True, blank=True, null=True, verbose_name='Creado por admin')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    profile = instance.profile
    # Si telephone es None o vacío, asignar el username
    if profile.telephone in (None, ''):
        profile.telephone = instance.username
    profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
