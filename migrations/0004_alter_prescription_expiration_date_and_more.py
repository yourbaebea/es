# Generated by Django 4.2 on 2023-05-18 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_medication_price_user_pharmacist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 17, 6, 12, 49, 756672, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='pharmacist',
            field=models.BooleanField(default=False),
        ),
    ]