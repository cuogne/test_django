# Generated by Django 5.0.6 on 2024-06-18 16:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_person_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]