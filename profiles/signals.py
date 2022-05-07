from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

import sqlite3
from datetime import datetime

# from PIL import Image
from django.core.files.images import ImageFile


def find_one(username):
    with sqlite3.connect(settings.BASE_DIR / "company_archive" / "db.sqlite") as conn:
        cur = conn.cursor()

        cur.execute(
            f"SELECT LastName, FirstName, FatherName, DateOfBirth, YearsOld, Phone, Email, Photo FROM Person WHERE Login = '{username}'"
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
                "1*rwKSSC1i2XjE4L5zbKUA5w.png",
                ImageFile(
                    open(
                        str(
                            settings.BASE_DIR
                            / "company_archive"
                            / "fake_photos"
                            / "1*rwKSSC1i2XjE4L5zbKUA5w.png"
                        ),
                        "rb",
                    )
                ),
            )
        else:
            info = find_one(instance.username)[0]
            profile = Profile.objects.create(
                user=instance,
                last_name=info[0],
                first_name=info[1],
                father_name=info[2],
                date_of_birth=datetime.strptime(info[3], "%d.%m.%Y"),
                years_old=info[4],
                phone=info[5],
                email=info[6],
            )
            profile.photo.save(
                info[7],
                ImageFile(
                    open(
                        str(
                            settings.BASE_DIR
                            / "company_archive"
                            / "fake_photos"
                            / info[7]
                        ),
                        "rb",
                    )
                ),
            )
