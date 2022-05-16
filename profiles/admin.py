from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "department",
        "position",
        "seniority",
        "company_seniority",
        "specialized_education",
        "additional_courses",
        "reprimands",
    ]
    search_fields = [
        "last_name",
        "first_name",
    ]


admin.site.register(Profile, ProfileAdmin)
