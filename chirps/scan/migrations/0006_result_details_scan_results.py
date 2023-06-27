# Generated by Django 4.2.2 on 2023-06-27 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("scan", "0005_result"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="details",
            field=models.JSONField(default="{}"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="scan",
            name="results",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="scan.result"
            ),
        ),
    ]
