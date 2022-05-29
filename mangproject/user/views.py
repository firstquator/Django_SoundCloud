from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
  if(request.method == "POST"):
    username = request.POST.get('username')
    password = request.POST.get('password')
    passwordCheck = request.POST.get('passwordCheck')

    if User.objects.filter(username = username).exists():
      return render(request, 'signup.html', {'error' : "이미 존재하는 사용자입니다."})

    if password == passwordCheck:
      user = User.objects.create_user(
        username = username,
        password = passwordCheck
      )
    else:
      return render(request, 'signup.html', {'error' : "비밀번호 확인이 일치하지 않습니다."})
    auth.login(request, user)
    return redirect('/')
  else:
    return render(request, 'signup.html')

def signin(request):
  if(request.method == "POST"):
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = auth.authenticate(request, username = username, password = password)

      if user is not None:
        auth.login(request, user)
        return redirect('/')
      else:
        return render(request, 'signin.html', { 'error': "사용자 이름 혹은 패스워드를 다시 확인해주세요." })
  else:
      return render(request, 'signup.html')
