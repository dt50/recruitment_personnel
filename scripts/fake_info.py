import requests

from pydantic import BaseModel, FilePath
from typing import Optional

from random import choice

from fake_generator import get_photo

import time

URL = "https://api.randomdatatools.ru?"

GENDER = {"man": "male", "woman": "female"}


class Person(BaseModel):
    LastName: str
    FirstName: str
    FatherName: str
    DateOfBirth: str
    YearsOld: str
    Phone: str
    Login: str
    Email: str
    PasportNum: str
    PasportCode: str
    PasportOtd: str
    PasportDate: str
    inn_fiz: str
    oms: int
    Address: str
    Country: str
    Region: str
    City: str
    Photo: Optional[FilePath] = None


def get_fake_person(id: int) -> Person:
    attributes = {
        "gender": choice(list(GENDER.keys())),
        "typeName": "all",
        "unescaped": "true",
        "params": "LastName,FirstName,FatherName,DateOfBirth,YearsOld,Phone,Login,Email,Address,Country,Region,City,PasportNum,PasportCode,PasportOtd,PasportDate,inn_fiz,oms",
    }
    ans = str(requests.get(URL, params=attributes).json())
    ans = ans.replace("'", '"')

    fake_person = Person.parse_raw(ans)

    Photo, state = get_photo(
        gender=GENDER[attributes["gender"]],
        FIO=[fake_person.LastName, fake_person.FirstName, fake_person.FatherName],
        id=id,
    )

    if state:
        time.sleep(5)
        Photo, _ = get_photo(
            gender=GENDER[attributes["gender"]],
            FIO=[fake_person.LastName, fake_person.FirstName, fake_person.FatherName],
            id=id,
        )

    fake_person.Photo = Photo

    if int(fake_person.YearsOld) > 60 or int(fake_person.YearsOld) < 20:
        get_fake_person(id)

    return fake_person


if __name__ == "__main__":
    print(list(get_fake_person(1)))
