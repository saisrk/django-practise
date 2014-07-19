from django.shortcuts import render
from django.template import loader, Context
from models import BlogPost
from django.http import HttpResponse

def archive(request):
    posts = BlogPost.objects.all()
    temp = loader.get_template('archive.html')
    cont = Context({'posts': posts})
    return HttpResponse(temp.render(cont))

def blog_home(request):
    latest_posts = BlogPost.objects.order_by('-timestamp')[:5]
    temp = loader.get_template('bloghome.html')
    cont = Context({"latest_posts": latest_posts})
    return HttpResponse(temp.render(cont))

def get_article(request, id):
    post = BlogPost.objects.get(pk=id)
    temp = loader.get_template("article.html")
    cont = Context({'post': post})
    return HttpResponse(temp.render(cont))
