# Generated by Django 5.0.1 on 2024-02-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0014_projects_alter_goals_body1_alter_goals_body2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='heading3',
            field=models.CharField(max_length=30),
        ),
    ]
