# Generated by Django 4.2.2 on 2023-06-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scan", "0007_remove_result_details_result_matches"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="matches",
        ),
        migrations.AddField(
            model_name="result",
            name="details",
            field=models.JSONField(default="{}"),
            preserve_default=False,
        ),
    ]
