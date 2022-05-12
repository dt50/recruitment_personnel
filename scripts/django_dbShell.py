from django.contrib.auth.models import User
from django.conf import settings

import sqlite3

from datetime import datetime

with sqlite3.connect(
    settings.BASE_DIR / "company_archive" / "db.sqlite"
) as conn:
    cur = conn.cursor()
    cur.execute("SELECT Login FROM Person")

    rows = cur.fetchall()
    cur.close()

row_1 = rows[0:500]
row_2 = rows[500:1000]

for i in row_1:
    user = User.objects.create_user(username=i[0], password="2121444")
    user.save()

for i in row_2:
    user = User.objects.create_user(username=i[0], password="2121444")
    user.save()
