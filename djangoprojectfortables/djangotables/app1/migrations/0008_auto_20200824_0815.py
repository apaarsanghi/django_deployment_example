# Generated by Django 3.1 on 2020-08-24 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20200824_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='drink_name',
            field=models.OneToOneField(default='123', on_delete=django.db.models.deletion.SET_DEFAULT, to='app1.item'),
        ),
    ]
