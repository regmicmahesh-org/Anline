# Generated by Django 3.1 on 2021-02-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_users', '0006_auto_20210129_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
