# Generated by Django 4.2.7 on 2023-12-03 22:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(7), django.core.validators.MaxLengthValidator(15)]),
        ),
    ]
