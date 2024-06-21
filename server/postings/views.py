from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from postings.forms import LoginForm
from postings.forms import PostForm
from postings.forms import CommentForm
from postings.models import PostModel, CommentModel

# test


def opt_page(request):
    context = {
        'pagename': 'Настройки',
    }

    return render(request, 'base/option.html', context)

def hello_page(request):
    context = {'pagename': 'Приветcтвенная страница!',}

    return render(request, 'hello.html', context)

def register_page(request):
    context = {'pagename': 'Регистрация',}

    if request.method == 'POST':
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()

            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        reg_form = UserCreationForm()

        context['reg_form'] = reg_form

    return render(request, 'registration/registration.html', context)

def login_page(request):
    context = {'pagename': 'Авторизация',}

    if request.method == 'GET':
        login_form = LoginForm(request.GET)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            login_form = LoginForm()

        context['login_form'] = login_form

    return render(request, 'registration/login.html', context)

def logout_page(request):
    logout(request)
    return redirect("/")

def post_list_page(request):
    context = {
        'pagename': 'Главная',
        'comment_form': CommentForm(),
    }

    filter = request.GET.get('filter', '')
    order_by = request.GET.get('order_by', 'created')
    if filter == '':
        posts = PostModel.objects.all().order_by(order_by).values()
    else:
        posts = PostModel.objects.filter(author_id=filter).order_by(order_by).values()
    for post in posts:
        post["comment_items"] = CommentModel.objects.filter(
            photo=post["id"]
        )
        post["author"] = User.objects.get(id=post["author_id"])
    context["post_items"] = posts

    return render(request, 'main.html', context)

def new_comment(request):
    context = {
        'comment_form': CommentForm()
    }

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.save(PostModel.objects.get(id=request.GET.get("post_id")),user=request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def posting_page(request):
    context = {
        'pagename': 'Оптравка поста',
    }

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        post_form.save(request.user)
    else:
        post_form = PostForm()

        context['post_form'] = post_form

    return render(request, 'post_add.html', context)

def post_page(request, id):
    context = {
        'pagename': 'Новость',

    }
    post = PostModel.objects.get(id=id)
    context['post'] = post
    comments = CommentModel.objects.filter(
        photo = id
    )
    context['comments'] = comments
    return render(request, 'post.html', context)

@login_required
def profile_page(request):
    context = {
        'pagename': 'user'
    }

    return render(request, 'accounts/profile_page.html', context)