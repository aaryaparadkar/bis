# Generated by Django 5.0.1 on 2024-02-05 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0019_alter_services_additional_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additional',
            name='additional',
        ),
        migrations.AddField(
            model_name='additional',
            name='service',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='additional_entries', to='bis.services'),
        ),
    ]
