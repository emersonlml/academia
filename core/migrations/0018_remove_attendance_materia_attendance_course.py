# Generated by Django 5.0.6 on 2024-06-04 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_registration_materia_registration_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='materia',
        ),
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Curso'),
        ),
    ]
