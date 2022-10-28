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
    return render(request, 'tsuda/syllabus_wordcloud.html', {'syllabus': syllabus})

# ここから
def akikyoshitsu_list(request):

    if request.POST:
        term = request.POST["term"]
        yobi = request.POST["yobi"]
        jigen = request.POST["jigen"]
        gokan = request.POST["gokan"]

        # classrooms = Classroom.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        classrooms = Classroom.objects.filter(term__contains = term, day_of_week__contains = yobi, period_of_time__contains = jigen)
        # print(classrooms)
        for allclass in classrooms:
            # allclass = Allclass.objects.all().exclude(class_number = '1111') # これは表示できる
            allclass = Allclass.objects.all().exclude(class_number = Classroom.class_number) # これだと全部表示されちゃう
    return render(request, 'tsuda/akikyoshitsu_list.html', {'allclass': allclass})
    # return render(request, 'tsuda/akikyoshitsu_list.html', {'classrooms': classrooms})
# ここまで
