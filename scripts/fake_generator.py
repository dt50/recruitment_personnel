import requests
import os
import random
import time
from pathlib import Path
from PIL import Image
from io import BytesIO


random.seed(time.time())
GENDER = ["male", "female"]
URL = "https://fakeface.rest/face/json?"
BASE_DIR = Path(__file__).resolve().parent.parent


def get_photo(*, FIO: list, gender: str, id: int) -> list[bool, str]:
    if gender not in GENDER:
        raise ValueError("Uncorrect gender")

    attributes = {
        "gender": gender,
        "minimum_age": 20,
        "maximum_age": 60,
    }

    try:
        ans = requests.get(URL, params=attributes).json()
        ans_url_to_photo = requests.get(ans["image_url"], stream=True).raw
    except Exception as e:
        print(e)
        return [None, True]

    os.chdir(BASE_DIR / "company_archive" / "fake_photos")

    img = Image.open(ans_url_to_photo)

    img = img.resize((216, 315), Image.Resampling.NEAREST)

    photo_name = f"{id}_{gender}_{FIO[0].capitalize()}_{FIO[1].capitalize()}_{FIO[2].capitalize()}_photo.jpg"

    img.save(photo_name)

    return [photo_name, False]


if __name__ == "__main__":
    print(get_photo(gender="female", FIO=["Anna", "Anna", "Anna"], id=1))
