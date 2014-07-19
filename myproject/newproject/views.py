from django.shortcuts import render
from django.template import loader, Context
from models import BlogPost
from django.http import HttpResponse

def archive(request):
    posts = BlogPost.objects.all()
    temp = loader.get_template('archive.html')
    cont = Context({'posts': posts})
    return HttpResponse(temp.render(cont))
