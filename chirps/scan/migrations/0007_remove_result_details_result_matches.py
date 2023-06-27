# Generated by Django 4.2.2 on 2023-06-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scan", "0006_result_details_scan_results"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="details",
        ),
        migrations.AddField(
            model_name="result",
            name="matches",
            field=models.CharField(default="", max_length=2048),
            preserve_default=False,
        ),
    ]
