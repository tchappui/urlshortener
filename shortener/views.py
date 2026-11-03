import random

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from .models import ShortLink


def generate_codes(code_key, code_date):
    seed = f"{code_date.isoformat()}+{code_key}"

    rng = random.Random(seed)

    return (
        rng.randint(100000, 999999),
        rng.randint(100000, 999999),
    )


def short_link(request, path):
    link = get_object_or_404(
        ShortLink,
        path=f"/{path}/",
    )

    if link.kind == ShortLink.Kind.REDIRECT:
        return redirect(link.url)

    codes = generate_codes(
        link.code_key,
        link.code_date,
    )

    return HttpResponse(
        f"<h1>{codes}</h1>",
        content_type="text/html; charset=utf-8",
    )
