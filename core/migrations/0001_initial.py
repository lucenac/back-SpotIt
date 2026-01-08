from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("lost", "Perdido"),
                            ("found", "Encontrado"),
                            ("returned", "Devolvido"),
                        ],
                        default="lost",
                        max_length=10,
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=255)),
                ("event_date", models.DateField(blank=True, null=True)),
                ("image_url", models.URLField(blank=True)),
                ("contact_info", models.CharField(blank=True, max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "reporter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reported_items",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
