# Generated by Django 5.0.1 on 2024-01-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0004_goals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('heading1', models.CharField(max_length=15)),
                ('content1', models.CharField(max_length=30)),
                ('heading2', models.CharField(max_length=15)),
                ('content2', models.CharField(max_length=30)),
                ('heading3', models.CharField(max_length=15)),
                ('content3', models.CharField(max_length=30)),
                ('heading4', models.CharField(max_length=15)),
                ('content4', models.CharField(max_length=30)),
            ],
        ),
    ]
