# Generated by Django 5.0.1 on 2024-02-05 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0017_services_additional_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('additional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bis.projects')),
            ],
        ),
    ]
