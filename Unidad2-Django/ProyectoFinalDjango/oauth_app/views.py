from django.shortcuts import render

# Create your views here.
def login_bootstrap(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')