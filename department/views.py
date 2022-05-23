from django.shortcuts import render
from django.views.generic import ListView

# models
from .models import Positions

# scripts
from .scripts.filters import (
    get_profile_promotions,
    profile_promotions_list,
    promotion_list,
)

import itertools


class TableView(ListView):
    template_name = "departments/table.html"
    queryset = Positions.objects.filter(count_person__lt=12)
    context_object_name = "query_results"


def promotion_position(request, pk):
    position = Positions.objects.get(pk=pk)

    profiles = get_profile_promotions(position)
    profile_list = profile_promotions_list(profiles)

    to_promotion = promotion_list(
        position.MAX_PERSON, position.count_person, profile_list
    )

    for employee in to_promotion:
        previously_pos = Positions.objects.get(position=employee.position)
        previously_pos.count_person -= 1
        previously_pos.save()

        new_pos = position

        employee.position = new_pos
        employee.save()

        new_pos.count_person += 1
        new_pos.save()

    return render(
        request,
        "departments/table2.html",
        context={
            "choose": to_promotion,
            "new_pos": position.position,
        },
    )
