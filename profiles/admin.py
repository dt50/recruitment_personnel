from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'department', 'position']


admin.site.register(Profile, ProfileAdmin)
