# Generated by Django 5.0.6 on 2024-06-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_materia_course_materias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='course',
            name='materias',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='average_trimester_1',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='average_trimester_2',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='average_trimester_3',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='final_average',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_1_trimester_1',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_1_trimester_2',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_1_trimester_3',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_2_trimester_1',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_2_trimester_2',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_2_trimester_3',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_3_trimester_1',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_3_trimester_2',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='mark_3_trimester_3',
        ),
        migrations.AddField(
            model_name='mark',
            name='average',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Promedio'),
        ),
        migrations.AddField(
            model_name='mark',
            name='mark_1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 1'),
        ),
        migrations.AddField(
            model_name='mark',
            name='mark_2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 2'),
        ),
        migrations.AddField(
            model_name='mark',
            name='mark_3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 3'),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
    ]
