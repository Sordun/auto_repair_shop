from datetime import date

from django.core.exceptions import ValidationError


def date_validator(value):
    """Проверка соответсвия даты записи"""
    today = date.today()

    if value.isoweekday() > 5:
        raise ValidationError("По выходным не работаем")
    if value < today:
        raise ValidationError("Дата не может быть раньше текущего дня")
    return value
