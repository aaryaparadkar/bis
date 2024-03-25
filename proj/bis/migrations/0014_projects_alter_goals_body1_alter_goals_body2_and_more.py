# Generated by Django 5.0.1 on 2024-02-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0013_remove_career_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(default='static/bis/images/5856.jpg', upload_to='images/')),
                ('tagline', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='goals',
            name='body1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='goals',
            name='body2',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='goals',
            name='body3',
            field=models.CharField(max_length=500),
        ),
    ]