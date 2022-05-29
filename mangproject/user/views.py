from django.shortcuts import render

# Create your views here.
def signup(request):
  if(request.method == "POST"):
    username = request.POST.get('username')
    password = request.POST.get('password')
    passwordCheck = request.POST.get('passwordCheck')
    

  return render(request, 'signup.html')

def signin(request):

  return render(request, 'signin.html')


