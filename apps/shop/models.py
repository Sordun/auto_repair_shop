from django.db import models
from django.contrib.auth.models import User

from shop.validators import date_validator


class Clients(models.Model):
    """Клиенты"""
    name = models.CharField(verbose_name="ФИО клиента", max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_model = models.CharField(verbose_name="Марка автомобиля", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Specialist(models.Model):
    """Специалист"""
    specialist_name = models.CharField(verbose_name="ФИО специалиста", max_length=100)

    def __str__(self):
        return self.specialist_name

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"


class CheckIn(models.Model):
    """Запись на диагностику"""

    class BusinessHours(models.IntegerChoices):
        """Часы приёма"""
        HOUR10 = 10, '10:00'
        HOUR11 = 11, '11:00'
        HOUR12 = 12, '12:00'
        HOUR13 = 13, '13:00'
        HOUR14 = 14, '14:00'
        HOUR15 = 15, '15:00'
        HOUR16 = 16, '16:00'
        HOUR17 = 17, '17:00'
        HOUR18 = 18, '18:00'
        HOUR19 = 19, '19:00'

    name = models.ForeignKey(Clients, verbose_name="ФИО клиента", on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, verbose_name="Специалист", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Дата приёма", validators=[date_validator])
    time = models.IntegerField(verbose_name="Время приёма", choices=BusinessHours.choices)
    is_complete = models.BooleanField(verbose_name="Выполнено", default=False)

    def __str__(self):
        return f"Запись № {self.id} сделал {self.specialist} на {self.date} в {self.time}"

    class Meta:
        verbose_name = "Запись приёма"
        verbose_name_plural = "Записи приёма"
        unique_together = ("date", "time", "specialist")
        ordering = ["date", "time", "specialist"]
