# Generated by Django 5.0.3 on 2024-03-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0002_game_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
