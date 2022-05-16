from profiles.models import Profile


def get_profile_promotions(position) -> dict:
    profiles = {
        "1": Profile.objects.all()
        .exclude(position=position)
        .filter(seniority__gt=30)
        .filter(company_seniority__gt=15)
        .filter(years_old__lt=60)
        .filter(specialized_education=1)
        .filter(additional_courses__gt=150)
        .filter(reprimands__lte=0),
        "2": Profile.objects.all()
        .exclude(position=position)
        .filter(seniority__gt=25)
        .filter(company_seniority__gt=15)
        .filter(years_old__lt=60)
        .filter(specialized_education=1)
        .filter(additional_courses__gt=100),
        "3": Profile.objects.all()
        .exclude(position=position)
        .filter(seniority__gt=20)
        .filter(company_seniority__gt=10)
        .filter(years_old__lt=60)
        .filter(specialized_education=1),
        "4": Profile.objects.all()
        .exclude(position=position)
        .filter(seniority__gt=10)
        .filter(company_seniority__gt=5)
        .filter(years_old__lt=60),
        "5": Profile.objects.all()
        .exclude(position=position)
        .filter(seniority__gt=5)
        .filter(company_seniority__gt=2),
        "6": Profile.objects.all().filter(seniority__gt=2).exclude(position=position),
    }
    return profiles


def profile_promotions_list(profiles_dict: dict) -> list:
    profiles_list = []
    for key, values in profiles_dict.items():
        for value in values:
            if value:
                profiles_list.append(value)
    return profiles_list


def promotion_list(max_person: int, count_person: int, profiles_list: list) -> set:
    to_promotion = set()
    for _ in range(int((max_person / 2)) - count_person):
        if profiles_list[0] not in to_promotion:
            to_promotion.add(profiles_list.pop(0))
        else:
            if profiles_list[1] not in to_promotion:
                to_promotion.add(profiles_list.pop(0))

    return to_promotion
