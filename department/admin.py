from django.contrib import admin
from .models import Departments, Positions
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'MIN_PERSON', 'count_person', 'MAX_PERSON']


class PositionAdmin(admin.ModelAdmin):
    list_display = ['position', 'MIN_PERSON', 'count_person', 'MAX_PERSON']


admin.site.register(Departments, DepartmentAdmin)
admin.site.register(Positions, PositionAdmin)
