from django.db import models

# Create your models here.


class Human(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите имя')
    surname = models.CharField(max_length=100, verbose_name='Введите фамилию')
    date_birth = models.DateField(verbose_name='Введите дату рождения')
    place_residence = models.CharField(max_length=200, verbose_name='Введите место проживания')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} {self.surname}'


class Man(Human):
    pass


class Woman(Human):
    pass
