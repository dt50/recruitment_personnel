import sqlite3
from pathlib import Path
import contextlib

from fake_info import get_fake_person

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR / "company_archive" / "db.sqlite")

raw_sql = """INSERT INTO Person (
    LastName, FirstName, FatherName, DateOfBirth, 
    YearsOld, Phone, Login, Email, PasportNum, 
    PasportCode, PasportOtd, PasportDate, inn_fiz, 
    oms, Address, Country, Region, 
    City, Photo
)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

create_table = """CREATE TABLE Person (
	id integer PRIMARY KEY AUTOINCREMENT,
	LastName string,
	FirstName text,
	FatherName text,
	DateOfBirth date,
	YearsOld integer,
	Phone text,
    Login text UNIQUE,
	Email text,
	PasportNum text,
	PasportCode text,
	PasportOtd text,
	PasportDate date,
	inn_fiz integer,
	oms integer,
	Address text,
	Country text,
	Region text,
	City text,
	Photo text
);"""

check_raw_sql = """SELECT id FROM Person WHERE Login = (?)"""


def generate_person(count=1000):
    with contextlib.closing(
        sqlite3.connect(BASE_DIR / "company_archive" / "db.sqlite")
    ) as conn:
        cur = conn.cursor()

        try:
            cur.execute(create_table)
        except sqlite3.OperationalError:
            print("Уже есть")

        for id in range(count):
            fake_person = get_fake_person(id)
            login = list()
            login.append(fake_person.Login)
            print(
                id, fake_person.LastName, fake_person.FirstName, fake_person.FatherName
            )
            cur.execute(check_raw_sql, login)
            unique = cur.fetchall()
            if len(unique) == 0:
                cur.execute(raw_sql, list(fake_person.dict().values()))
                conn.commit()
            else:
                continue
        cur.close()


if __name__ == "__main__":
    generate_person(100)
