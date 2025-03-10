# Generated by Django 5.0.4 on 2024-05-04 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("name", models.CharField(max_length=100)),
                ("carbs", models.FloatField()),
                ("Protein", models.FloatField()),
                ("fats", models.FloatField()),
                ("calories", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Consume",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "food_consumed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.food"
                    ),
                ),
            ],
        ),
    ]
