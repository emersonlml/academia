# Generated by Django 5.0.6 on 2024-05-31 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_trimester_mark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='average',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='trimester_1',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='trimester_2',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='trimester_3',
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester1_average',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Promedio Trimestre 1'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester1_mark1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 1 Trimestre 1'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester1_mark2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 2 Trimestre 1'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester1_mark3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 3 Trimestre 1'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester2_average',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Promedio Trimestre 2'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester2_mark1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 1 Trimestre 2'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester2_mark2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 2 Trimestre 2'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester2_mark3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 3 Trimestre 2'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester3_average',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Promedio Trimestre 3'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester3_mark1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 1 Trimestre 3'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester3_mark2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 2 Trimestre 3'),
        ),
        migrations.AddField(
            model_name='mark',
            name='trimester3_mark3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 3 Trimestre 3'),
        ),
    ]