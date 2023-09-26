# Generated by Django 4.2.5 on 2023-09-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0004_customuser_is_active_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
