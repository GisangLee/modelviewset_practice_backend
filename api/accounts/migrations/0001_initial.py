# Generated by Django 4.1 on 2022-08-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=20, unique=True)),
                ("email", models.EmailField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("m", "남"), ("f", "여")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("age", models.PositiveIntegerField(blank=True, null=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
