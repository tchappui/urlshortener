from django.core.exceptions import ValidationError
from django.db import models


class ShortLink(models.Model):
    class Kind(models.TextChoices):
        REDIRECT = "redirect", "Redirection"
        MONTHLY_CODE = "monthly_code", "Code"

    path = models.CharField(max_length=255, unique=True)

    kind = models.CharField(
        max_length=20,
        choices=Kind.choices,
        default=Kind.REDIRECT,
    )

    url = models.URLField(max_length=2048, blank=True)

    code_key = models.CharField(
        max_length=255,
        blank=True,
    )

    code_date = models.DateField(
        null=True,
        blank=True,
    )

    def clean(self):
        super().clean()

        self.path = f"/{self.path.strip().strip('/')}/"

        if self.path.startswith("/django-admin/"):
            raise ValidationError({"path": "Ce préfixe est réservé."})

        if self.kind == self.Kind.REDIRECT:
            if not self.url:
                raise ValidationError({"url": "Une URL est obligatoire."})

        elif self.kind == self.Kind.MONTHLY_CODE:
            errors = {}

            if not self.code_key:
                errors["code_key"] = "Une clé est obligatoire."

            if self.code_date is None:
                errors["code_date"] = "Une date est obligatoire."

            if errors:
                raise ValidationError(errors)

    def __str__(self):
        return self.path
