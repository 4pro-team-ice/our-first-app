# Generated by Django 3.2.15 on 2022-10-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsuda', '0037_auto_20221026_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='className',
            field=models.TextField(verbose_name='授業名'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='class_number',
            field=models.TextField(verbose_name='教室名'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='day_of_week',
            field=models.TextField(verbose_name='曜日'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='period_of_time',
            field=models.TextField(verbose_name='時限'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='term',
            field=models.TextField(verbose_name='ターム'),
        ),
    ]
