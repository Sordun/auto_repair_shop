from django.contrib import admin
from shop.models import CheckIn, Clients, Specialist


class CheckInInline(admin.TabularInline):
    model = CheckIn
    extra = 0


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ("specialist_name",)
    inlines = [CheckInInline]


admin.site.register(CheckIn)
admin.site.register(Clients)
