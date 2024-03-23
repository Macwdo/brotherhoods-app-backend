# Generated by Django 5.0.3 on 2024-03-23 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("game_day", models.DateTimeField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Player",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                (
                    "surname",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "alias",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("is_monthly_player", models.BooleanField(default=False)),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PlayerBill",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("due_date", models.DateTimeField()),
                ("payed_date", models.DateTimeField()),
                (
                    "payed_value",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=5
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="bills",
                        to="app_platform.player",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PlayersGames",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("as_monthly_player", models.BooleanField(default=False)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="games",
                        to="app_platform.game",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="games",
                        to="app_platform.player",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
