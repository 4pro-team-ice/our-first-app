# Generated by Django 3.2.15 on 2022-11-08 02:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tsuda', '0043_syllabuscomment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allclass',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='monday1',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='syllabuscomment',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
