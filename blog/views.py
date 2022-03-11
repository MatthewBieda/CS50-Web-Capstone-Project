from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, FormView

from blog.forms import CommentsForm, ArticleForm
from blog.models import User
from blog.models import Article, User, Comments, Reading_List
import json

class lgin(LoginView):
    template_name = "blog/login.html"

class lgout(LogoutView):
    template_name = "blog/index.html"

def index(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "blog/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "blog/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "blog/register.html")

class newarticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/newarticle.html"
    success_url = reverse_lazy("articles")

class listarticles(ListView):
    model = Article
    template_name = "blog/articles.html"

def detailarticle(request, pk):

    article = Article.objects.get(id=pk)
    comments_for_post = Comments.objects.filter(post_id=pk)
    commentsform = CommentsForm()

    if request.method == 'GET':
        commentsform = CommentsForm()

    if request.method == "POST":
        commentsform = CommentsForm(request.POST)
        if commentsform.is_valid():
            commentdraftform = commentsform.save(commit=False)
            commentdraftform.user = request.user
            commentdraftform.post = article
            commentsform.save()
            return HttpResponseRedirect(request.path_info)

    #handling add to reading list event 
    if(request.GET.get('addreadinglist')):
        foo = Reading_List()
        foo.user = request.user
        foo.savedpost = article
        foo.save()
        return HttpResponseRedirect(reverse('readinglist'))

    if request.method == "PUT":
        body_data = json.loads(request.body)

        postid = body_data['id']
        print(postid)
        updatedpost = body_data['content']
        print(updatedpost)
        Comments.objects.filter(id=postid).update(contents=updatedpost)

    
    #Checking if item already in watchlist
    user = request.user
    if user.is_authenticated:
        readinglistvalidate = article.reading_list_set.filter(user=user)

        context = {
            "article": article,
            "comments": comments_for_post,
            "commentsform": commentsform,
            "readinglist": readinglistvalidate
        }

        return render(request, "blog/article_detail.html", context)

    context = {
        "article": article,
        "comments": comments_for_post,
        "commentsform": commentsform,
    }
    return render(request, "blog/article_detail.html", context)

def readinglist(request):

    #get current user
    user = request.user

    #get this user's reading list
    reading_list = Reading_List.objects.filter(user_id=user.id)
    
    context = {
        'reading_list': reading_list
    }

    # Handling remove from watchlist event
    if request.GET.get('ModelRef'):
        readinglistpk = request.GET.get('ModelRef')
        record = Reading_List.objects.get(id=readinglistpk)
        record.delete()
        return HttpResponseRedirect(request.path_info)

    return render(request, "blog/readinglist.html", context)
    
