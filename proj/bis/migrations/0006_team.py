# Generated by Django 5.0.1 on 2024-01-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0005_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name1', models.CharField(max_length=20)),
                ('designation1', models.CharField(max_length=20)),
                ('name2', models.CharField(max_length=20)),
                ('designation2', models.CharField(max_length=20)),
                ('name3', models.CharField(max_length=20)),
                ('designation3', models.CharField(max_length=20)),
            ],
        ),
    ]
