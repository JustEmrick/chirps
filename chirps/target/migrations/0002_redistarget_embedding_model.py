# Generated by Django 4.2.3 on 2023-07-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redisasset',
            name='embedding_model',
            field=models.CharField(default='text-embedding-ada-002', max_length=256),
        ),
    ]
