from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from shop.models import CheckIn, Client, Specialist


class CheckInInline(admin.TabularInline):
    model = CheckIn
    extra = 0


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [CheckInInline]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "car_model",
    )
    fields = (
        "name",
        "user",
        "car_model",
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields["user"].disabled = True
        return form

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        clients = request.user.clients
        if request.user.id:
            return qs.filter(id=clients.id)

        return qs.none()


admin.site.register(CheckIn)
