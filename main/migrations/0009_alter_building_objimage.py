# Generated by Django 4.1.2 on 2023-04-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_rename_buildingsids_workgroup_buildings_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="building",
            name="objImage",
            field=models.ImageField(default="default/default.png", upload_to="images/"),
        ),
    ]