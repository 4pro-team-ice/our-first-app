# Generated by Django 3.2.15 on 2022-10-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsuda', '0007_syllabuscomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabuscomment',
            name='class_name',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]