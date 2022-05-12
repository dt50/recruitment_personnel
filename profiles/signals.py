# Django
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Models
from .models import Profile
from django.contrib.auth.models import User
from department.models import Departments, Positions

import sqlite3
from datetime import datetime

# from PIL import Image
from django.core.files.images import ImageFile


def find_one(username):
    with sqlite3.connect(settings.BASE_DIR / "company_archive" / "db.sqlite") as conn:
        cur = conn.cursor()

        cur.execute(
            f"SELECT LastName, FirstName, FatherName, DateOfBirth, YearsOld, Phone, Login,  Email, PasportNum, PasportCode, PasportOtd, PasportDate, inn_fiz, oms, Address, Country, Region, City, Photo FROM Person WHERE Login = '{username}'"
        )

        row = cur.fetchall()

        cur.close()

    return row


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser == 1:
            profile = Profile.objects.create(user=instance)
            profile.photo.save(
                "admin_photo.png",
                ImageFile(
                    open(
                        str(
                            settings.BASE_DIR
                            / "company_archive"
                            / "fake_photos"
                            / "admin_photo.png"
                        ),
                        "rb",
                    )
                ),
            )
        else:
            info = find_one(instance.username)
            info = info[0]

            profile = Profile.objects.create(
                user=instance,
                last_name=info[0],
                first_name=info[1],
                father_name=info[2],
                date_of_birth=datetime.strptime(info[3], "%d.%m.%Y"),
                years_old=info[4],
                phone=info[5],
                login=info[6],
                email=info[7],
                PasportNum=info[8],
                PasportCode=info[9],
                PasportOtd=info[10],
                PasportDate=info[11],
                inn_fiz=info[12],
                oms=info[13],
                Address=info[14],
                Country=info[15],
                Region=info[16],
                City=info[17],
            )
            profile.photo.save(
                info[18],
                ImageFile(
                    open(
                        str(
                            settings.BASE_DIR
                            / "company_archive"
                            / "fake_photos"
                            / info[18]
                        ),
                        "rb",
                    )
                ),
            )


@receiver(post_save, sender=Profile)
def post_save_update_department(sender, instance, created, **kwargs):
    if instance.department and instance.position:
        dep = Departments.objects.get(department_name=instance.department)
        pos = Positions.objects.get(position=instance.position)
        if dep.count_person < dep.MAX_PERSON and pos.count_person < pos.MAX_PERSON:
            dep.count_person += 1
            dep.save()
            pos.count_person += 1
            pos.save()
        else:
            instance.position = None
