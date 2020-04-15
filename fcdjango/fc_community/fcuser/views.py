from .models import Fcuser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('Home!')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not (username and password):
            res_data['error'] = '값을 입력해주세요.'
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id
                # 비밀번호가 일치, 로그인 처리
                return redirect('/')
            else:
                res_data['error'] = '비밀번호를 틀렸습니다'

        return render(request, 'login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)


        res_data = {}
        
        if not (username and useremail and password and re_password):
            res_data['error'] = '값을 입력해주세요.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)

            )

            fcuser.save()

        return render(request, 'register.html', res_data)