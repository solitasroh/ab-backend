# Generated by Django 4.1.1 on 2022-10-07 11:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
    ]