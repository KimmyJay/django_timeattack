from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .models import UserModel

# def base_response(request):
#     return HttpResponse("안녕하세요! 장고의 시작입니다!")

def signup(request):
    if request.method == 'GET':
        return render(request, 'index (1).html')
    # elif request.method =='POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # UserModel.objects.create_user(username=username, password=password)




