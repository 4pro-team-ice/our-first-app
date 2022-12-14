from django.conf import settings
from django.db import models
from django.utils import timezone
# ユーザー認証
from django.contrib.auth.models import User


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
    day_of_week = models.TextField(verbose_name='曜日')
    period_of_time = models.TextField(verbose_name='時限')
    className = models.TextField(verbose_name='授業名')
    term = models.TextField(verbose_name='ターム')
    class_number = models.TextField(verbose_name='教室名')
    # building_number = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.class_number

    class Meta:
       db_table = 'Classroom'
       verbose_name = 'Classroom'
       verbose_name_plural = 'Classroom'

class Allclass(models.Model):
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    class_number = models.TextField(verbose_name='教室名')
    # building_number = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.class_number
    class Meta:
        db_table = 'Allclass'
        verbose_name = 'Allclass'
        verbose_name_plural = 'Allclass'

class T1(models.Model):
    #inquiry_id = models.IntegerField(verbose_name='day')
    author_jikanwari = models.TextField(blank=True, null=True, verbose_name='作成者')

    class Day_Of_Week(): #曜日にIDを与える
        Monday = '0'
        Tuesday = '1'
        Wednesday = '2'
        Thursday = '3'
        Friday = '4'

    DAY_OF_WEEK_CHOICES = ( #IDと曜日の表示名を紐付け
        (Day_Of_Week.Monday, '月'),
        (Day_Of_Week.Tuesday, '火'),
        (Day_Of_Week.Wednesday, '水'),
        (Day_Of_Week.Thursday, '木'),
        (Day_Of_Week.Friday, '金')
    )

    dow = models.CharField(verbose_name='曜日',
                            choices=DAY_OF_WEEK_CHOICES,
                            max_length=50)

    class Period_Of_Time(): #時限にIDを与える
        First = '0'
        Second = '1'
        Third = '2'
        Fourth = '3'
        Fifth = '4'
        Sixth = '5'

    PERIOD_OF_TIME_CHOICES = ( #IDと時限の表示名を紐付け
        (Period_Of_Time.First, '1限'),
        (Period_Of_Time.Second, '2限'),
        (Period_Of_Time.Third, '3限'),
        (Period_Of_Time.Fourth, '4限'),
        (Period_Of_Time.Fifth, '5限'),
        (Period_Of_Time.Sixth, '6限'),
    )

    pot = models.CharField(verbose_name='時限',
                            choices=PERIOD_OF_TIME_CHOICES,
                            max_length=50)
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    className = models.TextField(verbose_name='授業名' , default = '--', blank=True, null=True)
    class_number = models.TextField(verbose_name='教室名', default = '--', blank=True, null=True)
    profName = models.TextField(verbose_name='教授名', default = '--',blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.className
    class Meta:
       db_table = 'T1'
       verbose_name = 'T1'
       verbose_name_plural = 'T1'

class T2(models.Model):
    author_jikanwari_2 = models.TextField(blank=True, null=True, verbose_name='作成者')

    class Day_Of_Week(): #曜日にIDを与える
        Monday = '0'
        Tuesday = '1'
        Wednesday = '2'
        Thursday = '3'
        Friday = '4'

    DAY_OF_WEEK_CHOICES = ( #IDと曜日の表示名を紐付け
        (Day_Of_Week.Monday, '月'),
        (Day_Of_Week.Tuesday, '火'),
        (Day_Of_Week.Wednesday, '水'),
        (Day_Of_Week.Thursday, '木'),
        (Day_Of_Week.Friday, '金')
    )

    dow = models.CharField(verbose_name='曜日',
                            choices=DAY_OF_WEEK_CHOICES,
                            max_length=50)

    class Period_Of_Time(): #時限にIDを与える
        First = '0'
        Second = '1'
        Third = '2'
        Fourth = '3'
        Fifth = '4'
        Sixth = '5'

    PERIOD_OF_TIME_CHOICES = ( #IDと時限の表示名を紐付け
        (Period_Of_Time.First, '1限'),
        (Period_Of_Time.Second, '2限'),
        (Period_Of_Time.Third, '3限'),
        (Period_Of_Time.Fourth, '4限'),
        (Period_Of_Time.Fifth, '5限'),
        (Period_Of_Time.Sixth, '6限'),
    )

    pot = models.CharField(verbose_name='時限',
                            choices=PERIOD_OF_TIME_CHOICES,
                            max_length=50)
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    className = models.TextField(verbose_name='授業名' , default = '--', blank=True, null=True)
    class_number = models.TextField(verbose_name='教室名', default = '--', blank=True, null=True)
    profName = models.TextField(verbose_name='教授名', default = '--',blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.className
    class Meta:
        db_table = 'T2'
        verbose_name = 'T2'
        verbose_name_plural = 'T2'

class T3(models.Model):
    author_jikanwari_3 = models.TextField(blank=True, null=True, verbose_name='作成者')

    class Day_Of_Week(): #曜日にIDを与える
        Monday = '0'
        Tuesday = '1'
        Wednesday = '2'
        Thursday = '3'
        Friday = '4'

    DAY_OF_WEEK_CHOICES = ( #IDと曜日の表示名を紐付け
        (Day_Of_Week.Monday, '月'),
        (Day_Of_Week.Tuesday, '火'),
        (Day_Of_Week.Wednesday, '水'),
        (Day_Of_Week.Thursday, '木'),
        (Day_Of_Week.Friday, '金')
    )

    dow = models.CharField(verbose_name='曜日',
                            choices=DAY_OF_WEEK_CHOICES,
                            max_length=50)

    class Period_Of_Time(): #時限にIDを与える
        First = '0'
        Second = '1'
        Third = '2'
        Fourth = '3'
        Fifth = '4'
        Sixth = '5'

    PERIOD_OF_TIME_CHOICES = ( #IDと時限の表示名を紐付け
        (Period_Of_Time.First, '1限'),
        (Period_Of_Time.Second, '2限'),
        (Period_Of_Time.Third, '3限'),
        (Period_Of_Time.Fourth, '4限'),
        (Period_Of_Time.Fifth, '5限'),
        (Period_Of_Time.Sixth, '6限'),
    )

    pot = models.CharField(verbose_name='時限',
                            choices=PERIOD_OF_TIME_CHOICES,
                            max_length=50)
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    className = models.TextField(verbose_name='授業名' , default = '--', blank=True, null=True)
    class_number = models.TextField(verbose_name='教室名', default = '--', blank=True, null=True)
    profName = models.TextField(verbose_name='教授名', default = '--',blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.className
    class Meta:
        db_table = 'T3'
        verbose_name = 'T3'
        verbose_name_plural = 'T3'

class T4(models.Model):
    author_jikanwari_4 = models.TextField(blank=True, null=True, verbose_name='作成者')

    class Day_Of_Week(): #曜日にIDを与える
        Monday = '0'
        Tuesday = '1'
        Wednesday = '2'
        Thursday = '3'
        Friday = '4'

    DAY_OF_WEEK_CHOICES = ( #IDと曜日の表示名を紐付け
        (Day_Of_Week.Monday, '月'),
        (Day_Of_Week.Tuesday, '火'),
        (Day_Of_Week.Wednesday, '水'),
        (Day_Of_Week.Thursday, '木'),
        (Day_Of_Week.Friday, '金')
    )

    dow = models.CharField(verbose_name='曜日',
                            choices=DAY_OF_WEEK_CHOICES,
                            max_length=50)

    class Period_Of_Time(): #時限にIDを与える
        First = '0'
        Second = '1'
        Third = '2'
        Fourth = '3'
        Fifth = '4'
        Sixth = '5'

    PERIOD_OF_TIME_CHOICES = ( #IDと時限の表示名を紐付け
        (Period_Of_Time.First, '1限'),
        (Period_Of_Time.Second, '2限'),
        (Period_Of_Time.Third, '3限'),
        (Period_Of_Time.Fourth, '4限'),
        (Period_Of_Time.Fifth, '5限'),
        (Period_Of_Time.Sixth, '6限'),
    )

    pot = models.CharField(verbose_name='時限',
                            choices=PERIOD_OF_TIME_CHOICES,
                            max_length=50)
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    className = models.TextField(verbose_name='授業名' , default = '--', blank=True, null=True)
    class_number = models.TextField(verbose_name='教室名', default = '--', blank=True, null=True)
    profName = models.TextField(verbose_name='教授名', default = '--',blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.className

    class Meta:
        db_table = 'T4'
        verbose_name = 'T4'
        verbose_name_plural = 'T4'


class Syllabus(models.Model):
    #授業ID
    #on_delete=CASCADE:ユーザーのアカウントが削除されたら同時に投稿内容も削除される
    classID = models.TextField() #科目番号
    className = models.TextField() #科目名
    className_eng = models.TextField() #科目名(英語)
    teacher_name = models.TextField() # 担当者名
    term = models.TextField() # 開講ターム
    tanni = models.TextField() # 単位
    gengo = models.TextField() # 使用言語
    nenji = models.TextField() # 配当年次
    bunya = models.TextField() # 学問分野
    level = models.TextField() # 推奨レベル
    gakka = models.TextField() # 科目区分
    syllabusinfo = models.TextField() # 講義の目的と内容
    mokuhyo = models.TextField() # 授業の到達目標
    keikaku = models.TextField() # 授業計画
    text = models.TextField() # テキスト
    sankosho = models.TextField() # 参考書
    junbi = models.TextField() # 準備学習の内容
    hyoka = models.TextField() # 評価方法・基準
    feedback = models.TextField() # 課題に対するフィードバック
    office_hour = models.TextField() # オフィスアワー
    tokushoku = models.TextField() # 授業の特色
    sonota = models.TextField() # その他

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.className

    class Meta:
        db_table = 'Syllabus'
        verbose_name = 'Syllabus'
        verbose_name_plural = 'Syllabus'


class SyllabusComment(models.Model): #シラバス用のコメント
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    className = models.TextField(verbose_name='授業名') #授業名
    kyoin_name = models.TextField(verbose_name='教員名') #教員名
    juko_year = models.TextField(verbose_name='受講年度' , blank=True, null=True) #受講年度

    class Test_or_Report(): #IDを与える
        Test = '0'
        Report = '1'
        Nothing = '2'

    TEST_OR_REPORT_CHOICES = ( #IDと紐付け
        (Test_or_Report.Test, 'テスト'),
        (Test_or_Report.Report, 'レポート'),
        (Test_or_Report.Nothing, 'なし'),
    )

    tor = models.CharField(verbose_name='テスト or レポート',
    choices=TEST_OR_REPORT_CHOICES,
    max_length=50)


    class Learning_Manegemet_System():
        Moodle = '0'
        Google_Classroom = '1'
        Portfolio = '2'
        Else = '3'
        Nothing = '4'

    LEARNING_MANEGMENT_SYSTEM_CHOICES = (
        (Learning_Manegemet_System.Moodle, 'moodle'),
        (Learning_Manegemet_System.Google_Classroom, 'Google Classroom'),
        (Learning_Manegemet_System.Portfolio, 'ポートフォリオ'),
        (Learning_Manegemet_System.Else, 'その他'),
        (Learning_Manegemet_System.Nothing, 'なし')
    )

    lms = models.CharField(verbose_name='学習管理システム',
    choices = LEARNING_MANEGMENT_SYSTEM_CHOICES,
    max_length=50)

    class Assignment_amont(): #IDを与える
        Too_much = '0'
        Much = '1'
        Normal = '2'
        Little = '3'
        Too_little = '4'
        Nothing = '5'

    ASSIGNMENT_AMOUNT_CHOICES = (
        (Assignment_amont.Too_much, 'とても多い'),
        (Assignment_amont.Much, '多い'),
        (Assignment_amont.Normal, '普通'),
        (Assignment_amont.Little, '少ない'),
        (Assignment_amont.Too_little, 'ほとんどない'),
        (Assignment_amont.Nothing, 'ない'),
    )

    aa = models.CharField(verbose_name='課題量',
    choices=ASSIGNMENT_AMOUNT_CHOICES,
    max_length=50)

    comment = models.TextField(verbose_name='コメント' , blank=True, null=True) #自由にコメント

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#管理画面に表示されるモデル内のデータ(レコード)を判別するための、名前(文字列)を定義する
        return self.className

    class Meta:
        db_table = 'SyllabusComment'
        verbose_name = 'SyllabusComment'
        verbose_name_plural = 'SyllabusComment'

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    gakka = models.CharField(max_length=10)
    gakunen = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Account'
        verbose_name = 'Account'
        verbose_name_plural = 'Account'
