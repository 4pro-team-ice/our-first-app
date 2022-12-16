# Generated by Django 3.2.15 on 2022-12-16 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.TextField(verbose_name='教室名')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.TextField(verbose_name='曜日')),
                ('period_of_time', models.TextField(verbose_name='時限')),
                ('className', models.TextField(verbose_name='授業名')),
                ('term', models.TextField(verbose_name='ターム')),
                ('class_number', models.TextField(verbose_name='教室名')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Akikyoushitu',
                'verbose_name_plural': 'Akikyoushitu',
                'db_table': 'Akikyoushitu',
            },
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classID', models.TextField()),
                ('className', models.TextField()),
                ('className_eng', models.TextField()),
                ('teacher_name', models.TextField()),
                ('term', models.TextField()),
                ('tanni', models.TextField()),
                ('gengo', models.TextField()),
                ('nenji', models.TextField()),
                ('bunya', models.TextField()),
                ('level', models.TextField()),
                ('gakka', models.TextField()),
                ('syllabusinfo', models.TextField()),
                ('mokuhyo', models.TextField()),
                ('keikaku', models.TextField()),
                ('text', models.TextField()),
                ('sankosho', models.TextField()),
                ('junbi', models.TextField()),
                ('hyoka', models.TextField()),
                ('feedback', models.TextField()),
                ('office_hour', models.TextField()),
                ('tokushoku', models.TextField()),
                ('sonota', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Syllabus',
                'verbose_name_plural': 'Syllabus',
                'db_table': 'Syllabus',
            },
        ),
        migrations.CreateModel(
            name='T1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_jikanwari', models.TextField(blank=True, null=True, verbose_name='作成者')),
                ('dow', models.CharField(choices=[('0', '月'), ('1', '火'), ('2', '水'), ('3', '木'), ('4', '金')], max_length=50, verbose_name='曜日')),
                ('pot', models.CharField(choices=[('0', '1限'), ('1', '2限'), ('2', '3限'), ('3', '4限'), ('4', '5限'), ('5', '6限')], max_length=50, verbose_name='時限')),
                ('className', models.TextField(blank=True, default='-----', null=True, verbose_name='授業名')),
                ('class_number', models.TextField(blank=True, default='-----', null=True, verbose_name='教室名')),
                ('profName', models.TextField(blank=True, default='-----', null=True, verbose_name='教授名')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='T2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_jikanwari_2', models.TextField(blank=True, null=True, verbose_name='作成者')),
                ('dow', models.CharField(choices=[('0', '月'), ('1', '火'), ('2', '水'), ('3', '木'), ('4', '金')], max_length=50, verbose_name='曜日')),
                ('pot', models.CharField(choices=[('0', '1限'), ('1', '2限'), ('2', '3限'), ('3', '4限'), ('4', '5限'), ('5', '6限')], max_length=50, verbose_name='時限')),
                ('className', models.TextField(blank=True, default='-----', null=True, verbose_name='授業名')),
                ('class_number', models.TextField(blank=True, default='-----', null=True, verbose_name='教室名')),
                ('profName', models.TextField(blank=True, default='-----', null=True, verbose_name='教授名')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='T3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_jikanwari_3', models.TextField(blank=True, null=True, verbose_name='作成者')),
                ('dow', models.CharField(choices=[('0', '月'), ('1', '火'), ('2', '水'), ('3', '木'), ('4', '金')], max_length=50, verbose_name='曜日')),
                ('pot', models.CharField(choices=[('0', '1限'), ('1', '2限'), ('2', '3限'), ('3', '4限'), ('4', '5限'), ('5', '6限')], max_length=50, verbose_name='時限')),
                ('className', models.TextField(blank=True, default='-----', null=True, verbose_name='授業名')),
                ('class_number', models.TextField(blank=True, default='-----', null=True, verbose_name='教室名')),
                ('profName', models.TextField(blank=True, default='-----', null=True, verbose_name='教授名')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='T4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_jikanwari_4', models.TextField(blank=True, null=True, verbose_name='作成者')),
                ('dow', models.CharField(choices=[('0', '月'), ('1', '火'), ('2', '水'), ('3', '木'), ('4', '金')], max_length=50, verbose_name='曜日')),
                ('pot', models.CharField(choices=[('0', '1限'), ('1', '2限'), ('2', '3限'), ('3', '4限'), ('4', '5限'), ('5', '6限')], max_length=50, verbose_name='時限')),
                ('className', models.TextField(blank=True, default='-----', null=True, verbose_name='授業名')),
                ('class_number', models.TextField(blank=True, default='-----', null=True, verbose_name='教室名')),
                ('profName', models.TextField(blank=True, default='-----', null=True, verbose_name='教授名')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SyllabusComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.TextField(verbose_name='授業名')),
                ('kyoin_name', models.TextField(verbose_name='教員名')),
                ('juko_year', models.TextField(blank=True, null=True, verbose_name='受講年度')),
                ('tor', models.CharField(choices=[('0', 'テスト'), ('1', 'レポート'), ('2', 'なし')], max_length=50, verbose_name='テスト or レポート')),
                ('lms', models.CharField(choices=[('0', 'moodle'), ('1', 'Google Classroom'), ('2', 'ポートフォリオ'), ('3', 'その他'), ('4', 'なし')], max_length=50, verbose_name='学習管理システム')),
                ('aa', models.CharField(choices=[('0', 'とても多い'), ('1', '多い'), ('2', '普通'), ('3', '少ない'), ('4', 'ほとんどない'), ('5', 'ない')], max_length=50, verbose_name='課題量')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='コメント')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gakka', models.CharField(max_length=10)),
                ('gakunen', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
