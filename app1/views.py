# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app1.models import Post

class Home(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "home.html"
    paginate_by = 10
    ordering = ["-id"]

def handle_uploaded_file(f):
    with open('/home/web/static/pictures/%s' % f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
@csrf_exempt
def coverpp(request):
    filename =  request.FILES['avatar-2'].name
    #handle_uploaded_file(request.FILES["avatar-2"])
    picture_data = {
    "errno": 0,
    "data": [
        "/static/pictures/%s" % filename,
    ]
    }
    return JsonResponse(picture_data) 
@csrf_exempt
def pp(request):
    filename =  request.FILES['file'].name
    handle_uploaded_file(request.FILES["file"])
    picture_data = {
    "errno": 0,
    "data": [
        "/static/pictures/%s" % filename,
    ]
    }
    return JsonResponse(picture_data) 

@csrf_exempt
def ppp(request):
    title =  request.POST.get("title",None)
    content  =  request.POST.get("content",None)
    refer  =  request.POST.get("refer",None)
    print title,content
    if title and content:
        Post.objects.create(title=title,content=content)
    return HttpResponse("ppp")

class CreatePostView(View):
    context = {}
    template_name = "post_create.html"
    def get(self,request):
        return render(request,self.template_name,context=self.context)
