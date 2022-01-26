from django.contrib import admin
from shop.models import CheckIn, Clients, Specialist


class CheckInInline(admin.TabularInline):
    model = CheckIn
    extra = 0


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ("specialist_name",)
    inlines = [CheckInInline]


class ClientsAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "car_model",)


admin.site.register(CheckIn)
admin.site.register(Clients, ClientsAdmin)
