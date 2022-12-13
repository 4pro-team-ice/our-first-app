from django import forms

from .models import Post

from .models import T1

from .models import T2

from .models import T3

from .models import T4

from .models import SyllabusComment

from django.contrib.auth.models import User
from .models import Account


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class JikannwariForm1(forms.ModelForm):

    class Meta:
        model = T1
        fields = ('className', 'class_number' ,'profName')

class JikannwariForm2(forms.ModelForm):

    class Meta:
        model = T2
        fields = ('className', 'class_number' ,'profName')

class JikannwariForm3(forms.ModelForm):

    class Meta:
        model = T3
        fields = ('className', 'class_number' ,'profName')

class JikannwariForm4(forms.ModelForm):

    class Meta:
        model = T4
        fields = ('className', 'class_number' ,'profName')

class SyllabusCommentForm(forms.ModelForm):

    class Meta:
        model = SyllabusComment
        fields = ('className','kyoin_name', 'juko_year' ,'tor' , 'lms', 'aa' ,'comment')


class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード　　 ")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID　　 ",'email':"メールアドレス "}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('gakka','gakunen',)
        labels = {'gakka':"学科　　　　　 ",'gakunen':"学年　　　　　 ",}
