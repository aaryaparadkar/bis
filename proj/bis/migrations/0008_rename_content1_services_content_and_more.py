# Generated by Django 5.0.1 on 2024-01-24 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0007_carousel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='content1',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='heading1',
            new_name='heading',
        ),
        migrations.RemoveField(
            model_name='services',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='content3',
        ),
        migrations.RemoveField(
            model_name='services',
            name='content4',
        ),
        migrations.RemoveField(
            model_name='services',
            name='heading2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='heading3',
        ),
        migrations.RemoveField(
            model_name='services',
            name='heading4',
        ),
    ]