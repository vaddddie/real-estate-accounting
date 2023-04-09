# Generated by Django 4.1.2 on 2023-04-09 15:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0006_workgroup"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="workgroup",
            name="buildingsIds",
        ),
        migrations.RemoveField(
            model_name="workgroup",
            name="usernames",
        ),
        migrations.AddField(
            model_name="workgroup",
            name="buildingsIds",
            field=models.ManyToManyField(to="main.building"),
        ),
        migrations.AddField(
            model_name="workgroup",
            name="usernames",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
