# Generated by Django 3.2.15 on 2022-12-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsuda', '0004_auto_20221121_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'Akikyoushitu', 'verbose_name_plural': 'Akikyoushitu'},
        ),
        migrations.AlterModelOptions(
            name='syllabus',
            options={'verbose_name': 'Syllabus', 'verbose_name_plural': 'Syllabus'},
        ),
        migrations.RenameField(
            model_name='syllabus',
            old_name='day_of_week',
            new_name='bunya',
        ),
        migrations.RenameField(
            model_name='syllabus',
            old_name='period_of_time',
            new_name='className_eng',
        ),
        migrations.AddField(
            model_name='syllabus',
            name='feedback',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='gengo',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='hyoka',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='junbi',
            field=models.TextField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='keikaku',
            field=models.TextField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='level',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='mokuhyo',
            field=models.TextField(default=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='nenji',
            field=models.TextField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='office_hour',
            field=models.TextField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='sankosho',
            field=models.TextField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='sonota',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='tanni',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='text',
            field=models.TextField(default=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='tokushoku',
            field=models.TextField(default=14),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='classroom',
            table='Akikyoushitu',
        ),
        migrations.AlterModelTable(
            name='syllabus',
            table='Syllabus',
        ),
    ]
