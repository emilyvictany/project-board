# Generated by Django 4.2.3 on 2023-07-25 18:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0002_alter_project_owner"),
        ("tasks", "0002_alter_project_start_date"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Project",
            new_name="Task",
        ),
    ]
