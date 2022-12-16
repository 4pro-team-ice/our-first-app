from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import T1
from .models import T2
from .models import T3
from .models import T4
from .forms import JikannwariForm1
from .forms import JikannwariForm2
from .forms import JikannwariForm3
from .forms import JikannwariForm4
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

def move_to_jikannwari_term(request):
    return render(request, 'tsuda/jikannwari_term.html')

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
def t1_list(request):
    if request.POST:
        user = request.POST["user"]
        print(user)

    first = T1.objects.filter(author_jikanwari = user, pot = 0).order_by('dow')[0:5]
    second = T1.objects.filter(author_jikanwari = user,pot = 1).order_by('dow')[0:5]
    third = T1.objects.filter(author_jikanwari = user,pot = 2).order_by('dow')[0:5]
    fourth = T1.objects.filter(author_jikanwari = user,pot = 3).order_by('dow')[0:5]
    fifth = T1.objects.filter(author_jikanwari = user,pot = 4).order_by('dow')[0:5]
    sixth = T1.objects.filter(author_jikanwari = user,pot = 5).order_by('dow')[0:5]
    params = {'data1': first , 'data2': second , 'data3': third ,
              'data4': fourth , 'data5':fifth , 'data6':sixth}
    return render(request, 'tsuda/t1_list.html', params)

def t1_detail(request, pk):
    t1 = get_object_or_404(T1, pk=pk)
    return render(request, 'tsuda/t1_detail.html', {'t1': t1})

def t1_new(request):
    form = JikannwariForm1()
    return render(request, 'tsuda/t1_edit.html', {'form': form})

def t1_new(request):
    if request.method == "POST":
        form = JikannwariForm1(request.POST)
        if form.is_valid():
            t1 = form.save(commit=False)
            t1.published_date = timezone.now()
            t1.save()
            return redirect('t1_detail', pk=t1.pk)
    else:
        form = JikannwariForm1()
    return render(request, 'tsuda/t1_edit.html', {'form': form})

def t1_edit(request, pk):
    t1 = get_object_or_404(T1, pk=pk)
    if request.method == "POST":
        form = JikannwariForm1(request.POST, instance=t1)
        if form.is_valid():
            t1 = form.save(commit=False)
            t1.published_date = timezone.now()
            t1.save()
            return redirect('t1_detail', pk=t1.pk)
    else:
        form = JikannwariForm1(instance=t1)
    return render(request, 'tsuda/t1_edit.html', {'form': form})

def t2_list(request):
    if request.POST:
        user = request.POST["user"]
        print(user)

    first = T2.objects.filter(author_jikanwari_2 = user, pot = 0).order_by('dow')[0:5]
    second = T2.objects.filter(author_jikanwari_2 = user,pot = 1).order_by('dow')[0:5]
    third = T2.objects.filter(author_jikanwari_2 = user,pot = 2).order_by('dow')[0:5]
    fourth = T2.objects.filter(author_jikanwari_2 = user,pot = 3).order_by('dow')[0:5]
    fifth = T2.objects.filter(author_jikanwari_2 = user,pot = 4).order_by('dow')[0:5]
    sixth = T2.objects.filter(author_jikanwari_2 = user,pot = 5).order_by('dow')[0:5]
    params = {'data1': first , 'data2': second , 'data3': third ,
              'data4': fourth , 'data5':fifth , 'data6':sixth}
    return render(request, 'tsuda/t2_list.html', params)

def t2_detail(request, pk):
    t2 = get_object_or_404(T2, pk=pk)
    return render(request, 'tsuda/t2_detail.html', {'t2': t2})

def t2_new(request):
    form = JikannwariForm2()
    return render(request, 'tsuda/t2_edit.html', {'form': form})

def t2_new(request):
    if request.method == "POST":
        form = JikannwariForm2(request.POST)
        if form.is_valid():
            t2 = form.save(commit=False)
            t2.published_date = timezone.now()
            t2.save()
            return redirect('t2_detail', pk=t2.pk)
    else:
        form = JikannwariForm2()
    return render(request, 'tsuda/t2_edit.html', {'form': form})

def t2_edit(request, pk):
    t2 = get_object_or_404(T2, pk=pk)
    if request.method == "POST":
        form = JikannwariForm2(request.POST, instance=t2)
        if form.is_valid():
            t2 = form.save(commit=False)
            t2.published_date = timezone.now()
            t2.save()
            return redirect('t2_detail', pk=t2.pk)
    else:
        form = JikannwariForm2(instance=t2)
    return render(request, 'tsuda/t2_edit.html', {'form': form})

def t3_list(request):
    if request.POST:
        user = request.POST["user"]
        print(user)

    first = T3.objects.filter(author_jikanwari_3 = user, pot = 0).order_by('dow')[0:5]
    second = T3.objects.filter(author_jikanwari_3 = user,pot = 1).order_by('dow')[0:5]
    third = T3.objects.filter(author_jikanwari_3 = user,pot = 2).order_by('dow')[0:5]
    fourth = T3.objects.filter(author_jikanwari_3 = user,pot = 3).order_by('dow')[0:5]
    fifth = T3.objects.filter(author_jikanwari_3 = user,pot = 4).order_by('dow')[0:5]
    sixth = T3.objects.filter(author_jikanwari_3 = user,pot = 5).order_by('dow')[0:5]
    params = {'data1': first , 'data2': second , 'data3': third ,
              'data4': fourth , 'data5':fifth , 'data6':sixth}
    return render(request, 'tsuda/t3_list.html', params)

def t3_detail(request, pk):
    t3 = get_object_or_404(T3, pk=pk)
    return render(request, 'tsuda/t3_detail.html', {'t3': t3})

def t3_new(request):
    form = JikannwariForm3()
    return render(request, 'tsuda/t3_edit.html', {'form': form})

def t3_new(request):
    if request.method == "POST":
        form = JikannwariForm3(request.POST)
        if form.is_valid():
            t3 = form.save(commit=False)
            t3.published_date = timezone.now()
            t3.save()
            return redirect('t3_detail', pk=t3.pk)
    else:
        form = JikannwariForm3()
    return render(request, 'tsuda/t3_edit.html', {'form': form})

def t3_edit(request, pk):
    t3 = get_object_or_404(T3, pk=pk)
    if request.method == "POST":
        form = JikannwariForm3(request.POST, instance=t3)
        if form.is_valid():
            t3 = form.save(commit=False)
            t3.published_date = timezone.now()
            t3.save()
            return redirect('t3_detail', pk=t3.pk)
    else:
        form = JikannwariForm3(instance=t3)
    return render(request, 'tsuda/t3_edit.html', {'form': form})

def t4_list(request):
    if request.POST:
        user = request.POST["user"]
        print(user)

    first = T4.objects.filter(author_jikanwari_4 = user, pot = 0).order_by('dow')[0:5]
    second = T4.objects.filter(author_jikanwari_4 = user,pot = 1).order_by('dow')[0:5]
    third = T4.objects.filter(author_jikanwari_4 = user,pot = 2).order_by('dow')[0:5]
    fourth = T4.objects.filter(author_jikanwari_4 = user,pot = 3).order_by('dow')[0:5]
    fifth = T4.objects.filter(author_jikanwari_4 = user,pot = 4).order_by('dow')[0:5]
    sixth = T4.objects.filter(author_jikanwari_4 = user,pot = 5).order_by('dow')[0:5]
    params = {'data1': first , 'data2': second , 'data3': third ,
              'data4': fourth , 'data5':fifth , 'data6':sixth}
    return render(request, 'tsuda/t4_list.html', params)

def t4_detail(request, pk):
    t4 = get_object_or_404(T4, pk=pk)
    return render(request, 'tsuda/t4_detail.html', {'t4': t4})

def t4_new(request):
    form = JikannwariForm4()
    return render(request, 'tsuda/t4_edit.html', {'form': form})

def t4_new(request):
    if request.method == "POST":
        form = JikannwariForm4(request.POST)
        if form.is_valid():
            t4 = form.save(commit=False)
            t4.published_date = timezone.now()
            t4.save()
            return redirect('t4_detail', pk=t4.pk)
    else:
        form = JikannwariForm4()
    return render(request, 'tsuda/t4_edit.html', {'form': form})

def t4_edit(request, pk):
    t4 = get_object_or_404(T4, pk=pk)
    if request.method == "POST":
        form = JikannwariForm4(request.POST, instance=t4)
        if form.is_valid():
            t4 = form.save(commit=False)
            t4.published_date = timezone.now()
            t4.save()
            return redirect('t4_detail', pk=t4.pk)
    else:
        form = JikannwariForm4(instance=t4)
    return render(request, 'tsuda/t4_edit.html', {'form': form})

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
            syllabuscomment.author_comment = request.user
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
            syllabuscomment.author_comment = request.user
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
        # yobi = request.POST["yobi"]
        # jigen = request.POST["jigen"]

        # syllabuss = Syllabus.objects.filter(className__contains = kamoku , teacher_name__contains = kyoin).all()
        # syllabuss = Syllabus.objects.filter(className__contains = kamoku , teacher_name__contains = kyoin ,
        # day_of_week__contains = yobi , period_of_time__contains = jigen,
        # term__contains = term , gakka__contains = gakka).all()
        syllabuss = Syllabus.objects.filter(className__contains = kamoku , teacher_name__contains = kyoin ,
        term__contains = term , gakka__contains = gakka).all()
        syllabus_kekka = 'tsuda/syllabuskekka_list.html'

    return render(request, syllabus_kekka, {'syllabuss': syllabuss})

def syllabus_detail(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    # a = syllabus.keikaku
    syllabus.keikaku = syllabus.keikaku.replace('◆', "\n") #◆で改行
    return render(request, 'tsuda/syllabus_detail.html', {'syllabus': syllabus})

def syllabus_wordcloud(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    text = [syllabus.syllabusinfo,syllabus.mokuhyo]
    # 形態素解析（tokenize）をインスタンスにする
    t = Tokenizer()

    # 単語リスト
    noun = []
    others = []

    # 文章を形態素（token）に分ける
    for i in text:
        for token in t.tokenize(i):
            pos = token.part_of_speech.split(',')  # 品詞情報抜き出し
            if '名詞' == pos[0]:                    # 品詞名が名詞なら
                noun.append(token.base_form)      # nounに追加
            elif 'その他' == pos[0]:
                others.append(token.base_form)

    #非表示単語の設定
    stop_words = ['教科書','こと','よう','テキスト','講義','なか','ため','授業','の','ところ','目標','学習','学び','これら','が','それら','もの','紹介','理解','必要','受講','導入',
                    '教材','毎週','的',
                    'a','and','to','for','the','of','in','as','are','is','all','will','into','who','class','should','on','but','be','learn','how','This','this',
                    'course','students','these','their','willbe','those']

    #画像データの読み込み
    FILE_PATH = './tsuda/static/img/donuts.png' # ローカル用の画像パス
    # FILE_PATH = './nakano2022seminar.pythonanywhere.com/static/img/donuts.png' # pythonanywhere上の画像パス

    donuts_coloring = np.array(Image.open(FILE_PATH))

    # wordcloudの準備
    wc = WordCloud(background_color="white",  # 背景色
               max_words=85,             # 最大表示単語数
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
        return render(request, 'tsuda/base.html')


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
    return render(request, "tsuda/menupage.html",context=params)


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
        return render(request,"tsuda/register.html",context=self.params)

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

            if request.method == "POST":
                if "toroku" in request.POST:

                    first = []
                    for i in range(5):
                        obj = T1(dow=i,pot=0)
                        # first.append(obj)????


                    T1.objects.create(author_jikanwari = account.username, pot = 0, dow = 0)
                    T1.objects.create(author_jikanwari = account.username,pot = 0, dow = 1)
                    T1.objects.create(author_jikanwari = account.username,pot = 0, dow = 2)
                    T1.objects.create(author_jikanwari = account.username,pot = 0, dow = 3)
                    T1.objects.create(author_jikanwari = account.username,pot = 0, dow = 4)
                    T1.objects.create(author_jikanwari = account.username,pot = 1, dow = 0)
                    T1.objects.create(author_jikanwari = account.username,pot = 1, dow = 1)
                    T1.objects.create(author_jikanwari = account.username,pot = 1, dow = 2)
                    T1.objects.create(author_jikanwari = account.username,pot = 1, dow = 3)
                    T1.objects.create(author_jikanwari = account.username,pot = 1, dow = 4)
                    T1.objects.create(author_jikanwari = account.username,pot = 2, dow = 0)
                    T1.objects.create(author_jikanwari = account.username,pot = 2, dow = 1)
                    T1.objects.create(author_jikanwari = account.username,pot = 2, dow = 2)
                    T1.objects.create(author_jikanwari = account.username,pot = 2, dow = 3)
                    T1.objects.create(author_jikanwari = account.username,pot = 2, dow = 4)
                    T1.objects.create(author_jikanwari = account.username,pot = 3, dow = 0)
                    T1.objects.create(author_jikanwari = account.username,pot = 3, dow = 1)
                    T1.objects.create(author_jikanwari = account.username,pot = 3, dow = 2)
                    T1.objects.create(author_jikanwari = account.username,pot = 3, dow = 3)
                    T1.objects.create(author_jikanwari = account.username,pot = 3, dow = 4)
                    T1.objects.create(author_jikanwari = account.username,pot = 4, dow = 0)
                    T1.objects.create(author_jikanwari = account.username,pot = 4, dow = 1)
                    T1.objects.create(author_jikanwari = account.username,pot = 4, dow = 2)
                    T1.objects.create(author_jikanwari = account.username,pot = 4, dow = 3)
                    T1.objects.create(author_jikanwari = account.username,pot = 4, dow = 4)
                    T1.objects.create(author_jikanwari = account.username,pot = 5, dow = 0)
                    T1.objects.create(author_jikanwari = account.username,pot = 5, dow = 1)
                    T1.objects.create(author_jikanwari = account.username,pot = 5, dow = 2)
                    T1.objects.create(author_jikanwari = account.username,pot = 5, dow = 3)
                    T1.objects.create(author_jikanwari = account.username,pot = 5, dow = 4)


                    T2.objects.create(author_jikanwari = account.username, pot = 0, dow = 0)
                    T2.objects.create(author_jikanwari = account.username,pot = 0, dow = 1)
                    T2.objects.create(author_jikanwari = account.username,pot = 0, dow = 2)
                    T2.objects.create(author_jikanwari = account.username,pot = 0, dow = 3)
                    T2.objects.create(author_jikanwari = account.username,pot = 0, dow = 4)
                    T2.objects.create(author_jikanwari = account.username,pot = 1, dow = 0)
                    T2.objects.create(author_jikanwari = account.username,pot = 1, dow = 1)
                    T2.objects.create(author_jikanwari = account.username,pot = 1, dow = 2)
                    T2.objects.create(author_jikanwari = account.username,pot = 1, dow = 3)
                    T2.objects.create(author_jikanwari = account.username,pot = 1, dow = 4)
                    T2.objects.create(author_jikanwari = account.username,pot = 2, dow = 0)
                    T2.objects.create(author_jikanwari = account.username,pot = 2, dow = 1)
                    T2.objects.create(author_jikanwari = account.username,pot = 2, dow = 2)
                    T2.objects.create(author_jikanwari = account.username,pot = 2, dow = 3)
                    T2.objects.create(author_jikanwari = account.username,pot = 2, dow = 4)
                    T2.objects.create(author_jikanwari = account.username,pot = 3, dow = 0)
                    T2.objects.create(author_jikanwari = account.username,pot = 3, dow = 1)
                    T2.objects.create(author_jikanwari = account.username,pot = 3, dow = 2)
                    T2.objects.create(author_jikanwari = account.username,pot = 3, dow = 3)
                    T2.objects.create(author_jikanwari = account.username,pot = 3, dow = 4)
                    T2.objects.create(author_jikanwari = account.username,pot = 4, dow = 0)
                    T2.objects.create(author_jikanwari = account.username,pot = 4, dow = 1)
                    T2.objects.create(author_jikanwari = account.username,pot = 4, dow = 2)
                    T2.objects.create(author_jikanwari = account.username,pot = 4, dow = 3)
                    T2.objects.create(author_jikanwari = account.username,pot = 4, dow = 4)
                    T2.objects.create(author_jikanwari = account.username,pot = 5, dow = 0)
                    T2.objects.create(author_jikanwari = account.username,pot = 5, dow = 1)
                    T2.objects.create(author_jikanwari = account.username,pot = 5, dow = 2)
                    T2.objects.create(author_jikanwari = account.username,pot = 5, dow = 3)
                    T2.objects.create(author_jikanwari = account.username,pot = 5, dow = 4)

                    T3.objects.create(author_jikanwari = account.username, pot = 0, dow = 0)
                    T3.objects.create(author_jikanwari = account.username,pot = 0, dow = 1)
                    T3.objects.create(author_jikanwari = account.username,pot = 0, dow = 2)
                    T3.objects.create(author_jikanwari = account.username,pot = 0, dow = 3)
                    T3.objects.create(author_jikanwari = account.username,pot = 0, dow = 4)
                    T3.objects.create(author_jikanwari = account.username,pot = 1, dow = 0)
                    T3.objects.create(author_jikanwari = account.username,pot = 1, dow = 1)
                    T3.objects.create(author_jikanwari = account.username,pot = 1, dow = 2)
                    T3.objects.create(author_jikanwari = account.username,pot = 1, dow = 3)
                    T3.objects.create(author_jikanwari = account.username,pot = 1, dow = 4)
                    T3.objects.create(author_jikanwari = account.username,pot = 2, dow = 0)
                    T3.objects.create(author_jikanwari = account.username,pot = 2, dow = 1)
                    T3.objects.create(author_jikanwari = account.username,pot = 2, dow = 2)
                    T3.objects.create(author_jikanwari = account.username,pot = 2, dow = 3)
                    T3.objects.create(author_jikanwari = account.username,pot = 2, dow = 4)
                    T3.objects.create(author_jikanwari = account.username,pot = 3, dow = 0)
                    T3.objects.create(author_jikanwari = account.username,pot = 3, dow = 1)
                    T3.objects.create(author_jikanwari = account.username,pot = 3, dow = 2)
                    T3.objects.create(author_jikanwari = account.username,pot = 3, dow = 3)
                    T3.objects.create(author_jikanwari = account.username,pot = 3, dow = 4)
                    T3.objects.create(author_jikanwari = account.username,pot = 4, dow = 0)
                    T3.objects.create(author_jikanwari = account.username,pot = 4, dow = 1)
                    T3.objects.create(author_jikanwari = account.username,pot = 4, dow = 2)
                    T3.objects.create(author_jikanwari = account.username,pot = 4, dow = 3)
                    T3.objects.create(author_jikanwari = account.username,pot = 4, dow = 4)
                    T3.objects.create(author_jikanwari = account.username,pot = 5, dow = 0)
                    T3.objects.create(author_jikanwari = account.username,pot = 5, dow = 1)
                    T3.objects.create(author_jikanwari = account.username,pot = 5, dow = 2)
                    T3.objects.create(author_jikanwari = account.username,pot = 5, dow = 3)
                    T3.objects.create(author_jikanwari = account.username,pot = 5, dow = 4)


                    T4.objects.create(author_jikanwari = account.username, pot = 0, dow = 0)
                    T4.objects.create(author_jikanwari = account.username,pot = 0, dow = 1)
                    T4.objects.create(author_jikanwari = account.username,pot = 0, dow = 2)
                    T4.objects.create(author_jikanwari = account.username,pot = 0, dow = 3)
                    T4.objects.create(author_jikanwari = account.username,pot = 0, dow = 4)
                    T4.objects.create(author_jikanwari = account.username,pot = 1, dow = 0)
                    T4.objects.create(author_jikanwari = account.username,pot = 1, dow = 1)
                    T4.objects.create(author_jikanwari = account.username,pot = 1, dow = 2)
                    T4.objects.create(author_jikanwari = account.username,pot = 1, dow = 3)
                    T4.objects.create(author_jikanwari = account.username,pot = 1, dow = 4)
                    T4.objects.create(author_jikanwari = account.username,pot = 2, dow = 0)
                    T4.objects.create(author_jikanwari = account.username,pot = 2, dow = 1)
                    T4.objects.create(author_jikanwari = account.username,pot = 2, dow = 2)
                    T4.objects.create(author_jikanwari = account.username,pot = 2, dow = 3)
                    T4.objects.create(author_jikanwari = account.username,pot = 2, dow = 4)
                    T4.objects.create(author_jikanwari = account.username,pot = 3, dow = 0)
                    T4.objects.create(author_jikanwari = account.username,pot = 3, dow = 1)
                    T4.objects.create(author_jikanwari = account.username,pot = 3, dow = 2)
                    T4.objects.create(author_jikanwari = account.username,pot = 3, dow = 3)
                    T4.objects.create(author_jikanwari = account.username,pot = 3, dow = 4)
                    T4.objects.create(author_jikanwari = account.username,pot = 4, dow = 0)
                    T4.objects.create(author_jikanwari = account.username,pot = 4, dow = 1)
                    T4.objects.create(author_jikanwari = account.username,pot = 4, dow = 2)
                    T4.objects.create(author_jikanwari = account.username,pot = 4, dow = 3)
                    T4.objects.create(author_jikanwari = account.username,pot = 4, dow = 4)
                    T4.objects.create(author_jikanwari = account.username,pot = 5, dow = 0)
                    T4.objects.create(author_jikanwari = account.username,pot = 5, dow = 1)
                    T4.objects.create(author_jikanwari = account.username,pot = 5, dow = 2)
                    T4.objects.create(author_jikanwari = account.username,pot = 5, dow = 3)
                    T4.objects.create(author_jikanwari = account.username,pot = 5, dow = 4)

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"tsuda/register.html",context=self.params)
