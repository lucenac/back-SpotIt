from django.conf import settings
from django.db import models


class Item(models.Model):
    class Type(models.TextChoices):
        LOST = "lost", "Perdido"
        FOUND = "found", "Encontrado"

    class Status(models.TextChoices):
        ACTIVE = "active", "Ativo"
        RESOLVED = "resolved", "Resolvido"

    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.LOST,
    )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    category = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True, blank=True)
    contact_name = models.CharField(max_length=150, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    image_url = models.URLField(blank=True)
    resolved_by = models.CharField(max_length=255, null=True, blank=True)
    resolved_contact = models.CharField(max_length=255, blank=True)
    resolved_contact_type = models.CharField(
        max_length=10,
        choices=[("email", "Email"), ("phone", "Telefone")],
        blank=True,
    )
    resolved_notes = models.TextField(blank=True)
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reported_items",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.status})"
