# Generated by Django 3.2.15 on 2022-10-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsuda', '0011_merge_20221004_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]