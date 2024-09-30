# Generated by Django 5.0.7 on 2024-09-17 14:41

import qrapp.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedLoginAttempts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255, unique=True)),
                ('attempts', models.PositiveBigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='phone_no',
            field=qrapp.models.PhoneNumberField(max_length=15, null=True, region='IN'),
        ),
        migrations.AlterField(
            model_name='register',
            name='visit_id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='visite_time',
            field=models.DateTimeField(null=True),
        ),
    ]