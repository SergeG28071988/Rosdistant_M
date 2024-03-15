# Generated by Django 5.0.3 on 2024-03-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Введите имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Введите фамилию')),
                ('date_birth', models.DateField(verbose_name='Введите дату рождения')),
                ('place_residence', models.CharField(max_length=200, verbose_name='Введите место проживания')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Введите имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Введите фамилию')),
                ('date_birth', models.DateField(verbose_name='Введите дату рождения')),
                ('place_residence', models.CharField(max_length=200, verbose_name='Введите место проживания')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
