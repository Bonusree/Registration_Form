# Generated by Django 4.1.4 on 2023-02-07 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chairman',
            name='dept_name',
        ),
        migrations.RemoveField(
            model_name='hallprovost',
            name='hall_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dept_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='student',
            name='session_start_year',
        ),
    ]