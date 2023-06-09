# Generated by Django 4.2.1 on 2023-06-02 21:54

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
                ("phone_number", models.CharField(max_length=20)),
                ("city", models.CharField(max_length=100)),
                ("last_login", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Pet",
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
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
                ("breed", models.CharField(max_length=100)),
                ("deceased_date", models.DateField(blank=True, null=True)),
                ("owner", models.ManyToManyField(related_name="pets", to="pets.user")),
            ],
        ),
    ]
