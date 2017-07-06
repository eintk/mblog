# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.http import HttpResponse
from .models import Post
from django.shortcuts import redirect
from django.template.loader import get_template


# Create your views here.
def homepage(request):
    template=get_template('index.html')
    posts=Post.objects.all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)


def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post !=None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')