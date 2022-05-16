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
from random import choice, randint

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

            dep = Departments.objects.get(pk=1)
            pos = choice(Positions.objects.all())
            _seniority = randint(0, info[4] - 20)

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
                pasportNum=info[8],
                pasportCode=info[9],
                pasportOtd=info[10],
                pasportDate=info[11],
                inn_fiz=info[12],
                oms=info[13],
                address=info[14],
                country=info[15],
                region=info[16],
                city=info[17],
                department=dep,
                position=pos,
                seniority=_seniority,
                company_seniority=randint(0, _seniority),
                specialized_education=randint(0, 1),
                additional_courses=randint(0, 200),
                reprimands=randint(0, 2),
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
            dep.count_person += 1
            pos.count_person += 1
            dep.save()
            pos.save()
