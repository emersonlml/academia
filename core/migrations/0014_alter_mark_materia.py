# Generated by Django 5.0.6 on 2024-06-01 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.materia', verbose_name='Materia'),
        ),
    ]
