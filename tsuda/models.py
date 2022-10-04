from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.title

class Classroom(models.Model):
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    classID = models.TextField()
    #title = models.CharField(max_length=200)
    #text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    class_number = models.TextField()
    building_number = models.TextField()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.class_number

class Monday1(models.Model):
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    className = models.TextField()#授業名
    class_number = models.TextField()#教室名
    profName = models.TextField()#教授名
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.className

class Monday2(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Monday3(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Monday4(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Monday5(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Monday6(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Tuesday1(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Tuesday2(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Tuesday3(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Tuesday4(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Tuesday5(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Tuesday6(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Wednesday1(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Wednesday2(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Wednesday3(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Wednesday4(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Wednesday5(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Wednesday6(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Thursday1(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Thursday2(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Thursday3(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Thursday4(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Thursday5(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Thursday6(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Friday1(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Friday2(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Friday3(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Friday4(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Friday5(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Friday6(models.Model):
    className = models.TextField()
    class_number = models.TextField()
    profName = models.TextField()

    def __str__(self):
        return self.className

class Syllabus(models.Model):
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    classID = models.TextField() #授業ID
    class_name = models.TextField() #授業名

    term_1 = models.TextField() #開講ターム
    term_2 = models.TextField() #開講ターム
    term_3 = models.TextField() #開講ターム
    term_4 = models.TextField() #開講ターム
    day_of_week = models.TextField() #曜日
    period_of_time = models.TextField() #時限
    teacher_name = models.TextField() #教員名
    #ここから学科の名前
    eibun = models.TextField()
    kokkan = models.TextField()
    tabunka = models.TextField()
    sugaku = models.TextField()
    johou = models.TextField()

    syllabus_info = models.TextField()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.class_name


class SyllabusComment(models.Model): #シラバスのコメント用
    class_name = models.TextField() #授業名
    juko_year = models.TextField() #受講年度
    test_or_report = models.TextField() #テストかレポート
    jugyo_document = models.TextField() #Google Classroom か moodle か ポートフォリオか
    kadai_ryo = models.TextField() #課題の量
    comment = models.TextField() #自由にコメント


    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.class_name
