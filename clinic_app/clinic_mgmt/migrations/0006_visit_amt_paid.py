# Generated by Django 3.0.6 on 2020-06-03 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_mgmt', '0005_visit_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='amt_paid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
