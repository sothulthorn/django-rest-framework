# Generated by Django 5.1.6 on 2025-02-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="branch",
            field=models.CharField(max_length=50),
        ),
    ]
