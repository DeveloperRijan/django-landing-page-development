# Generated by Django 3.2.4 on 2021-07-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_package_packagefeature_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagefeature',
            name='price',
        ),
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
