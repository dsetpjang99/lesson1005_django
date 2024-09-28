from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):
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

    return render(request, "user/register.html", {"form": form, "message": message})
