from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import Monday1
from .forms import JikannwariForm
from .models import SyllabusComment
from .forms import SyllabusCommentForm
from .models import Syllabus
from .models import Classroom
from .models import Allclass

from django.views.generic import TemplateView #テンプレートタグ
from .forms import AccountForm, AddAccountForm #ユーザーアカウントフォーム
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#ワードクラウド用ライブラリ
from janome.tokenizer import Tokenizer
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib,cv2
import matplotlib.pyplot as plt
import sys
sys.path.append('../')





# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tsuda/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'tsuda/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'tsuda/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'tsuda/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'tsuda/post_edit.html', {'form': form})

#画面遷移の動作
def move_to_menupage(request):
    return render(request, 'tsuda/menupage.html')

def move_to_jikannwari(request):
    return render(request, 'tsuda/jikannwari.html')

def move_to_akikyoshitsu(request):
    return render(request, 'tsuda/akikyoshitsu.html')

def move_to_akikyoshitsukekka(request):
    return render(request, 'tsuda/akikyoshitsukekka.html')

def move_to_syllabus(request):
    return render(request, 'tsuda/syllabus.html')

def move_to_map(request):
    return render(request, 'tsuda/map.html')

def move_to_eigyoujikan(request):
    return render(request, 'tsuda/eigyoujikan.html')

def move_to_jihanki(request):
    return render(request, 'tsuda/jihanki.html')

def move_to_honkan(request):
    return render(request, 'tsuda/honkan.html')

def move_to_shinkan(request):
    return render(request, 'tsuda/shinkan.html')

def move_to_minami(request):
    return render(request, 'tsuda/minami.html')

def move_to_tokkyo(request):
    return render(request, 'tsuda/tokkyo.html')

def move_to_ichigokan(request):
    return render(request, 'tsuda/ichigokan.html')

def move_to_gogokan(request):
    return render(request, 'tsuda/gogokan.html')

def move_to_nanagokan(request):
    return render(request, 'tsuda/nanagokan.html')

def move_to_library(request):
    return render(request, 'tsuda/library.html')

def move_to_shokudo(request):
    return render(request, 'tsuda/shokudo.html')

#時間割登録用
def monday1_list(request):
    # monday1s = Monday1.objects.all()
    first = Monday1.objects.filter(pot = 0).order_by('dow')[0:5]
    second = Monday1.objects.filter(pot = 1).order_by('dow')[0:5]
    third = Monday1.objects.filter(pot = 2).order_by('dow')[0:5]
    fourth = Monday1.objects.filter(pot = 3).order_by('dow')[0:5]
    fifth = Monday1.objects.filter(pot = 4).order_by('dow')[0:5]
    sixth = Monday1.objects.filter(pot = 5).order_by('dow')[0:5]
    params = {'data1': first , 'data2': second , 'data3': third ,
              'data4': fourth , 'data5':fifth , 'data6':sixth}
    return render(request, 'tsuda/monday1_list.html', params)

def monday1_detail(request, pk):
    monday1 = get_object_or_404(Monday1, pk=pk)
    return render(request, 'tsuda/monday1_detail.html', {'monday1': monday1})

def monday1_new(request):
    form = JikannwariForm()
    return render(request, 'tsuda/monday1_edit.html', {'form': form})

def monday1_new(request):
    if request.method == "POST":
        form = JikannwariForm(request.POST)
        if form.is_valid():
            monday1 = form.save(commit=False)
            monday1.author = request.user
            monday1.published_date = timezone.now()
            monday1.save()
            return redirect('monday1_detail', pk=monday1.pk)
    else:
        form = JikannwariForm()
    return render(request, 'tsuda/monday1_edit.html', {'form': form})

def monday1_edit(request, pk):
    monday1 = get_object_or_404(Monday1, pk=pk)
    if request.method == "POST":
        form = JikannwariForm(request.POST, instance=monday1)
        if form.is_valid():
            monday1 = form.save(commit=False)
            monday1.author = request.user
            monday1.published_date = timezone.now()
            monday1.save()
            return redirect('monday1_detail', pk=monday1.pk)
    else:
        form = JikannwariForm(instance=monday1)
    return render(request, 'tsuda/monday1_edit.html', {'form': form})

# シラバスコメント用
def syllabuscomment_list(request):

    if request.POST:
        className = request.POST["className"]
    syllabuscomments = SyllabusComment.objects.filter(className__contains = className, published_date__lte=timezone.now()).order_by('published_date').reverse()
    # syllabuscomments = SyllabusComment.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()

    return render(request, 'tsuda/syllabuscomment_list.html', {'syllabuscomments': syllabuscomments})

def syllabuscomment_detail(request, pk):
    syllabuscomment = get_object_or_404(SyllabusComment, pk=pk)
    return render(request, 'tsuda/syllabuscomment_detail.html', {'syllabuscomment': syllabuscomment})

def syllabuscomment_new(request):
    form = SyllabusCommentForm()
    return render(request, 'tsuda/syllabuscomment_edit.html', {'form': form})

def syllabuscomment_new(request):
    if request.method == "POST":
        form = SyllabusCommentForm(request.POST)
        if form.is_valid():
            syllabuscomment = form.save(commit=False)
            syllabuscomment.author = request.user
            syllabuscomment.published_date = timezone.now()
            syllabuscomment.save()
            return redirect('syllabuscomment_detail', pk=syllabuscomment.pk)
    else:
        form = SyllabusCommentForm()
    return render(request, 'tsuda/syllabuscomment_edit.html', {'form': form})

def syllabuscomment_edit(request, pk):
    syllabuscomment = get_object_or_404(SyllabusComment, pk=pk)
    if request.method == "POST":
        form = SyllabusCommentForm(request.POST, instance=syllabuscomment)
        if form.is_valid():
            syllabuscomment = form.save(commit=False)
            syllabuscomment.author = request.user
            syllabuscomment.published_date = timezone.now()
            syllabuscomment.save()
            return redirect('syllabuscomment_detail', pk=syllabuscomment.pk)
    else:
        form = SyllabusCommentForm(instance=syllabuscomment)
    return render(request, 'tsuda/syllabuscomment_edit.html', {'form': form})

def move_to_syllabuskensaku(request):
    return render(request, 'tsuda/syllabuskensaku.html')

def move_to_syllabuskekka(request):
    return render(request, 'tsuda/syllabuskekka.html')

def move_to_syllabuskamoku(request):
    return render(request, 'tsuda/syllabuskamoku.html')

def move_to_syllabuswordcloud(request):
    return render(request, 'tsuda/syllabuswordcloud.html')

def syllabuskekka_list(request):
    # syllabuss = Syllabus.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'tsuda/syllabuskekka_list.html', {'syllabuss': syllabuss})

    if request.POST:
        gakka = request.POST["gakka"]
        kamoku = request.POST["kamoku"]
        kyoin = request.POST["kyoin"]
        term = request.POST["term"]
        yobi = request.POST["yobi"]
        jigen = request.POST["jigen"]

        # syllabuss = Syllabus.objects.filter(className__contains = kamoku , teacher_name__contains = kyoin).all()
        syllabuss = Syllabus.objects.filter(className__contains = kamoku , teacher_name__contains = kyoin ,
        day_of_week__contains = yobi , period_of_time__contains = jigen,
        term__contains = term , gakka__contains = gakka).all()
        syllabus_kekka = 'tsuda/syllabuskekka_list.html'

    return render(request, syllabus_kekka, {'syllabuss': syllabuss})

def syllabus_detail(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    return render(request, 'tsuda/syllabus_detail.html', {'syllabus': syllabus})

def syllabus_wordcloud(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    text = syllabus.syllabusinfo
    # 形態素解析（tokenize）をインスタンスにする
    t = Tokenizer()

    # 単語リスト
    noun = []
    others = []

    # 文章を形態素（token）に分ける
    for token in t.tokenize(text):
        pos = token.part_of_speech.split(',')  # 品詞情報抜き出し
        if '名詞' == pos[0]:                    # 品詞名が名詞なら
            noun.append(token.base_form)      # nounに追加
        elif 'その他' == pos[0]:
            others.append(token.base_form)

    #非表示単語の設定
    stop_words = ['教科書','こと','よう','テキスト','講義','なか','ため','授業','の','ところ','目標','学習','学び','これら']

    #画像データの読み込み
    FILE_PATH = './tsuda/static/img/donuts.png' # ローカル用の画像パス
    # FILE_PATH = './nakano2022seminar.pythonanywhere.com/static/img/donuts.png' # pythonanywhere上の画像パス

    donuts_coloring = np.array(Image.open(FILE_PATH))

    # wordcloudの準備
    wc = WordCloud(background_color="white",  # 背景色
               max_words=100,             # 最大表示単語数
               max_font_size=100,         # 最大フォントサイズ
               random_state=42,           # 乱数設定
               font_path="/Library/Fonts//Arial Unicode.ttf", # ローカル用のフォントパス
               # font_path=r'/usr/share/fonts/truetype/fonts-japanese-gothic.ttf' # pythonanywhere上のフォントパス
               mask=donuts_coloring,
               colormap='tab10',
               stopwords=stop_words) # フォント

    text = " ".join(noun)

    # 文章をword cloudに読み込ませる
    wc.generate(text)
    wc.to_file('./tsuda/static/img/wordcloud.png') # ローカル上の画像パス
    # wc.to_file('./nakano2022seminar.pythonanywhere.com/static/img/wordcloud.png') # pythonanywhere上の画像パス


    return render(request, 'tsuda/syllabus_wordcloud.html', {'syllabus': syllabus})


def akikyoshitsu_list(request):

    if request.POST:
        term = request.POST["term"]
        yobi = request.POST["yobi"]
        jigen = request.POST["jigen"]
        gokan = request.POST["gokan"]

        # classrooms = Classroom.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        classrooms = Classroom.objects.filter(term__contains = term, day_of_week__contains = yobi,
                                               period_of_time__contains = jigen).values("class_number")
        # for allclass in classrooms:
            # allclass = Allclass.objects.all().exclude(class_number = '1111') # これは表示できる
        allclass = Allclass.objects.filter(published_date__lte=timezone.now(), class_number__startswith=gokan).all().exclude(class_number__in = classrooms).order_by('published_date') # これだと全部表示されちゃう
    return render(request, 'tsuda/akikyoshitsu_list.html', {'allclass': allclass})
    # return render(request, 'tsuda/akikyoshitsu_list.html', {'classrooms': classrooms})


#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('move_to_menupage'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'Tsuda/base.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "Tsuda/menupage.html",context=params)


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"Tsuda/register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account


            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"Tsuda/register.html",context=self.params)
