# Generated by Django 3.2.4 on 2021-07-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210705_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]
