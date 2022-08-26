from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
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
#画面遷移の動作
def move_to_menupage(request):
    return render(request, 'tsuda/menupage.html')

def move_to_jikannwari(request):
    return render(request, 'tsuda/jikannwari.html')

def move_to_konnzatsu(request):
    return render(request, 'tsuda/konnzatsu.html')

def move_to_syllabus(request):
    return render(request, 'tsuda/syllabus.html')

def move_to_kyukou(request):
    return render(request, 'tsuda/kyukou.html')

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
