# Generated by Django 5.0.7 on 2024-08-04 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("realstudentapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subjects",
            name="Staffs_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="realstudentapp.staffs",
            ),
        ),
        migrations.AlterField(
            model_name="adminhod",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="courses",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="staffs",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
