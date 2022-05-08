# Generated by Django 4.0.4 on 2022-05-07 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneRagTime_app', '0002_alter_cashcall_iban'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='cashcall',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='investments',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
