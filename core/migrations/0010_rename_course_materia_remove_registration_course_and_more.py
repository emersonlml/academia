# Generated by Django 5.0.6 on 2024-06-01 23:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_materia_teacher_remove_course_materias_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Materia',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='course',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='student',
        ),
        migrations.AlterModelOptions(
            name='materia',
            options={'verbose_name': 'Materia', 'verbose_name_plural': 'Materias'},
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]