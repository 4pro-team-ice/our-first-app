# Generated by Django 3.2.15 on 2022-10-06 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsuda', '0016_monday1_pot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monday1',
            name='dow',
            field=models.IntegerField(choices=[(0, '月'), (1, '火'), (2, '水'), (3, '木'), (4, '金')], default=0, verbose_name='day_of_week'),
        ),
        migrations.AlterField(
            model_name='monday1',
            name='pot',
            field=models.IntegerField(choices=[(0, '1限'), (1, '2限'), (2, '3限'), (3, '4限'), (4, '5限'), (5, '6限')], default=0, verbose_name='period_of_time'),
        ),
    ]