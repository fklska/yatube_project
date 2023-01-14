from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Main page')


def group_list(request):
    return HttpResponse('Group list page')


def group_posts(request, slug):
    return HttpResponse('Group posts page')