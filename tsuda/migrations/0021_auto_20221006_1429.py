# Generated by Django 3.2.15 on 2022-10-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsuda', '0020_alter_monday1_pot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monday1',
            name='className',
            field=models.TextField(verbose_name='授業名'),
        ),
        migrations.AlterField(
            model_name='monday1',
            name='class_number',
            field=models.TextField(verbose_name='教室名'),
        ),
        migrations.AlterField(
            model_name='monday1',
            name='profName',
            field=models.TextField(verbose_name='教授名'),
        ),
    ]
