# Generated by Django 4.0.5 on 2023-06-13 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_remove_exercise_body_muscle_exercise_body_muscle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='program',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='Muscle',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
