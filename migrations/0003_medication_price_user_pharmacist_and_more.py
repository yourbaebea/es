# Generated by Django 4.2 on 2023-05-18 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_medication_price_remove_user_pharmacist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Price (€)'),
        ),
        migrations.AddField(
            model_name='user',
            name='pharmacist',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 17, 6, 11, 47, 496625, tzinfo=datetime.timezone.utc)),
        ),
    ]
