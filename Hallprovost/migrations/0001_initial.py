# Generated by Django 4.1.4 on 2023-03-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
