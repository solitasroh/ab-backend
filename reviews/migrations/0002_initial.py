# Generated by Django 4.1.1 on 2022-10-07 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reviews", "0001_initial"),
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rooms.room",
            ),
        ),
    ]