# Generated by Django 5.0.6 on 2024-09-18 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_unique_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='unique_code',
        ),
    ]
