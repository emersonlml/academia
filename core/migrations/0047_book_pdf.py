# Generated by Django 5.0.6 on 2024-12-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='books_pdfs/', verbose_name='Archivo PDF'),
        ),
    ]
