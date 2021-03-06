# Generated by Django 3.2.4 on 2021-07-05 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_packagefeature_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagefeature',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='packagefeature',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.package'),
        ),
    ]
