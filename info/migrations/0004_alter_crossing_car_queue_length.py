# Generated by Django 4.0.2 on 2022-03-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_news_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crossing',
            name='car_queue_length',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
