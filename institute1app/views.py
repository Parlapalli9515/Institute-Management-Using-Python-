from django.shortcuts import render, redirect
from .models import Form,Commet
from .admin import Coursedetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')

@login_required(login_url='login')
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url='login')
def contactpage(request):
    if request.method == 'GET':
        data=Form.objects.all()
        return render(request,'contactpage.html',{'siva':data})
    else:
        name1=request.POST['name']
        mobile1=request.POST['mobile']
        email1=request.POST['email']
        age1=request.POST['age']
        gender1=request.POST['gender']
        location1=request.POST['location']
        course1=request.POST['course']
        Form(
        name=name1,
        mobile=mobile1,
        email=email1,
        age=age1,
        gender=gender1,
        location=location1,
        course=course1,
        ).save()
        data=Form.objects.all()
        return render(request,'contactpage.html',{'siva':data})

@login_required(login_url='login')
def servicepage(request):
    courses = Coursedetails.objects.all()
    return render(request,'servicepage.html', {'ab':courses})

@login_required(login_url='login')
def feedbackpage(request):
    if request.method == 'GET':
        data = Commet.objects.all()
        return render(request,'feedbackpage.html', {'preethi':data})
    else:
        course1 = request.POST['course']
        Commet(
        commit=course1
        ).save()
        data= Commet.objects.all().order_by('-id')
        return render(request,'feedbackpage.html',{'preethi':data})

@login_required(login_url='login')
def gallerypage(request):
    return render(request,'gallerypage.html')

def loginPage(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(request, username=username1, password=password1)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login')

def logoutPage(request):
    logout(request)
    return redirect('mainpage')
