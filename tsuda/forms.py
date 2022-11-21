from django import forms

from .models import Post

from .models import Monday1

from .models import Monday2

from .models import Monday3

from .models import Monday4

from .models import SyllabusComment

from django.contrib.auth.models import User
from .models import Account


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class JikannwariForm1(forms.ModelForm):

    class Meta:
        model = Monday1
        fields = ('className', 'class_number' ,'profName')

class JikannwariForm2(forms.ModelForm):

    class Meta:
        model = Monday2
        fields = ('className', 'class_number' ,'profName')

class JikannwariForm3(forms.ModelForm):

    class Meta:
        model = Monday3
        fields = ('className', 'class_number' ,'profName')

class JikannwariForm4(forms.ModelForm):

    class Meta:
        model = Monday4
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
