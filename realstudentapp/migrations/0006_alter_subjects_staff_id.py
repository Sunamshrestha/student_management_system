# Generated by Django 5.0.7 on 2024-08-06 03:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("realstudentapp", "0005_alter_courses_updated_at_alter_staffs_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subjects",
            name="Staff_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
