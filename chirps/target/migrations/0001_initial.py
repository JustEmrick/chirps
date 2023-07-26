# Generated by Django 4.2.3 on 2023-07-19 13:51

import asset.custom_fields
import django.db.models.deletion
import fernet_fields.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTarget',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=128)),
                (
                    'polymorphic_ctype',
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='polymorphic_%(app_label)s.%(class)s_set+',
                        to='contenttypes.contenttype',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='MantiumTarget',
            fields=[
                (
                    'baseasset_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='asset.baseasset',
                    ),
                ),
                ('app_id', models.CharField(max_length=256)),
                ('client_id', models.CharField(max_length=256)),
                (
                    'client_secret',
                    fernet_fields.fields.EncryptedCharField(max_length=256),
                ),
                ('top_k', models.IntegerField(default=100)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('asset.baseasset',),
        ),
        migrations.CreateModel(
            name='PineconeTarget',
            fields=[
                (
                    'baseasset_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='asset.baseasset',
                    ),
                ),
                (
                    'api_key',
                    asset.custom_fields.CustomEncryptedCharField(max_length=256),
                ),
                (
                    'environment',
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ('index_name', models.CharField(blank=True, max_length=256, null=True)),
                (
                    'project_name',
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ('metadata_text_field', models.CharField(max_length=256, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('asset.baseasset',),
        ),
        migrations.CreateModel(
            name='RedisTarget',
            fields=[
                (
                    'baseasset_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='asset.baseasset',
                    ),
                ),
                ('host', models.CharField(max_length=1048)),
                ('port', models.PositiveIntegerField()),
                ('database_name', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(blank=True, max_length=2048, null=True)),
                ('index_name', models.CharField(max_length=256)),
                ('text_field', models.CharField(max_length=256)),
                ('embedding_field', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('asset.baseasset',),
        ),
    ]
