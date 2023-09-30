# Generated by Django 4.2.5 on 2023-09-30 10:57

import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0005_remove_customuser_is_active_customuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='picture',
            field=models.ImageField(default='image', upload_to='photos/%Y/%m/%d/', verbose_name='Фото поста'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2000, 1, 1), verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Стафф?'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Суперюзер?'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография профиля'),
        ),
    ]