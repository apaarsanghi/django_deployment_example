# Generated by Django 3.1 on 2020-08-24 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20200824_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='drink_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='menu_name',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, to='app1.menu'),
        ),
    ]
