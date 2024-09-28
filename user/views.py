from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import time


# Create your views here.


def user_logout(request):
    logout(request)

    # redirect 對應的網址名稱(使用urls.py的name去對應)
    # user\urls => path("login/", views.user_login, name="login" )
    return redirect("login")


def user_profile(request):
    return render(request, "user/profile.html")


def user_login(request):
    message = ""
    user = None
    username = request.session.get("username", "")

    if request.method == "POST":
        if request.POST.get("register"):
            # redirect 對應的網址名稱(使用urls.py的name去對應)
            # user\urls => path("register/", views.user_register, name="register" )
            return redirect("register")

        if request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")

            if username == "" or password == "":
                message = "帳號密碼不能為空!"
            else:
                user = authenticate(request, username=username, password=password)
                if user:
                    message = "登入成功!"
                    login(request, user)
                    
                    time.sleep(3)

                    # redirect 對應的網址名稱(使用urls.py的name去對應)
                    # user\urls => path("profile/", views.user_profile, name="profile" )
                    return redirect("profile")
                else:
                    message = "帳號或密碼錯誤!"

    return render(
        request,
        "user/login.html",
        {"message": message, "user": user, "username": username},
    )


def user_register(request):
    # return HttpResponse("<h1>Hello Django!</h1>")
    message = ""
    form = UserCreationForm()

    # all,get,filter
    print(User.objects.all())
    # print(User.objects.get(username="danny"))
    # print(User.objects.filter(username="danny"))

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 密碼長度8
        if len(password1) != 8 or len(password2) != 8:
            message = "密碼長度不正確"
        elif password1 != password2:
            message = "兩次密碼不一樣"
        else:
            # 比對使用者是否存在
            if User.objects.filter(username=username):
                message = "帳號已存在!"
            # 註冊使用者
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                message = "註冊成功!"
                request.session["username"] = user.username

                time.sleep(3)

                # redirect 對應的網址名稱(使用urls.py的name去對應)
                # user\urls => path("login/", views.user_login, name="login" )
                return redirect("login")

    return render(request, "user/register.html", {"form": form, "message": message})
