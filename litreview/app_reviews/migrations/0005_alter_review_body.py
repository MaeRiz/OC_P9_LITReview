# Generated by Django 3.2.2 on 2021-06-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reviews', '0004_auto_20210603_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192),
        ),
    ]
