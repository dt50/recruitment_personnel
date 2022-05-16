from django.shortcuts import render
from django.views.generic import ListView

# models
from .models import Positions

# scripts
from .scripts.filters import get_profile_promotions, profile_promotions_list


class TableView(ListView):
    template_name = "departments/table.html"
    queryset = Positions.objects.filter(count_person__lt=12)
    context_object_name = "query_results"


def promotion_position(request, pk):
    position = Positions.objects.get(pk=pk)

    profiles = get_profile_promotions(position)
    profile_list = profile_promotions_list(profiles)

    to_promotion = set()

    for _ in range(int((position.MAX_PERSON / 2)) - position.count_person):
        if profile_list[0] not in to_promotion:
            to_promotion.add(profile_list.pop(0))
        else:
            if profile_list[1] not in to_promotion:
                to_promotion.add(profile_list.pop(0))

    return render(
        request,
        "departments/table2.html",
        context={"query_results": profiles.items(), "choose": to_promotion},
    )
