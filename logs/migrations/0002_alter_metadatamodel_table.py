# Generated by Django 4.2.7 on 2023-11-17 10:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("logs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="metadatamodel",
            table="metadata",
        ),
    ]