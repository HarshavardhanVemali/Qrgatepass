# Generated by Django 5.0.7 on 2024-08-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0006_alter_register_visite_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='visite_time',
            field=models.DateTimeField(null=True),
        ),
    ]
