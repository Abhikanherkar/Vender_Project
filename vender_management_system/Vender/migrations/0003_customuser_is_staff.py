# Generated by Django 5.0.4 on 2024-05-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vender', '0002_alter_vender_average_response_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]