from django.db import models
from django.contrib.auth.models import User


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
    is_active = models.BooleanField(verbose_name="Доступен", default=True)

    def __str__(self):
        return self.specialist_name

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"


class CheckIn(models.Model):
    """Запись на диагностику"""
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    specialist = models.ForeignKey(Specialist, verbose_name="Специалист", on_delete=models.CASCADE)
    is_complete = models.BooleanField(verbose_name="Выполнено", default=False)
    created_by = models.ForeignKey(User, verbose_name="Создал", on_delete=models.CASCADE)
    name = models.ForeignKey(Clients, verbose_name="ФИО клиента", on_delete=models.CASCADE)

    def __str__(self):
        return f"Запись сделал {self.created_by}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
