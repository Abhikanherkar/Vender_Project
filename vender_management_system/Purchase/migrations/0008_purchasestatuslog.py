# Generated by Django 5.0.4 on 2024-05-07 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0007_alter_purchase_acknowledgment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseStatusLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('prchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_log', to='Purchase.purchase')),
            ],
        ),
    ]
