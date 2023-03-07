from django.shortcuts import render,HttpResponse
from .models import *
from rest_framework.views import APIView
import datetime


# Create your views here.

class create_diary(APIView):
    def post():
        diary = Diary()
        diary.title = request.data.get("title")
        diary.user = request.data.get("user")
        diary.post_pass = request.data.get("pass")
        diary.content = request.data.get("content")
        diary.created_at = datetime.datetime.now()