# Generated by Django 3.2.2 on 2021-06-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reviews', '0006_rename_content_ticket_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
