# Generated by Django 4.0.1 on 2022-01-26 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО клиента')),
                ('car_model', models.CharField(blank=True, max_length=200, null=True, verbose_name='Марка автомобиля')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist_name', models.CharField(max_length=100, verbose_name='ФИО специалиста')),
                ('date', models.DateField(verbose_name='Дата диагностики')),
                ('time', models.TimeField(verbose_name='Время диагностики')),
                ('clients_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.clients', verbose_name='ФИО клиента')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.clients', verbose_name='ФИО клиента')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.specialist', verbose_name='Специалист')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]