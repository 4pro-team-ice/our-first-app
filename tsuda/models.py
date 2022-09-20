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
