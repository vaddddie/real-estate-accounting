# Generated by Django 4.1.2 on 2023-04-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_building_objstatus_alter_building_objtype"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workgroup",
            fields=[
                (
                    "ID",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("topic", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("buildingsIds", models.CharField(max_length=150)),
                ("usernames", models.CharField(max_length=150)),
            ],
        ),
    ]
