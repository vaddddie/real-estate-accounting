# Generated by Django 4.1.2 on 2023-04-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_building_objimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="building",
            name="objStatus",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="building",
            name="objType",
            field=models.CharField(max_length=20),
        ),
    ]
