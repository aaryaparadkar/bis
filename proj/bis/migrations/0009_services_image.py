# Generated by Django 5.0.1 on 2024-01-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0008_rename_content1_services_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(default='static/bis/images/5856.jpg', upload_to='images/'),
        ),
    ]
