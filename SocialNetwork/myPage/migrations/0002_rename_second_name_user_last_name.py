# Generated by Django 4.2.5 on 2023-09-24 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
