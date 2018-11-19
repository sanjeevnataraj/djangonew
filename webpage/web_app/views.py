from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect
from web_app.forms import SignUpForm,Register,Hobbies
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student_profile,Hobby_details
from django.views.generic import View,ListView
from django.contrib.auth.models import User
from . import models

def index(request):
    return render(request,"homepage.html")
@login_required
def special(request):
    return HttpResponse("you are login successfully")
@login_required
def user_logout(requets):
    logout(requets)
    return HttpResponseRedirect(reverse('index'))

def registration_page(request):

    registered = False

    if request.method == "POST":

        signup_detail = SignUpForm(data=request.POST)
        student_detail = Register(data=request.POST)
        hobby = Hobbies(data=request.POST)

        if signup_detail.is_valid() and student_detail.is_valid() and hobby.is_valid():
            user = signup_detail.save()
            user.set_password(user.password)
            user.save()

            student = student_detail.save(commit=False)
            student.user = user

            if 'profile_pic' in request.FILES:
                student.profile_pic = request.FILES['profile_pic']
            student.save()

            hobby.save()
            registered = True
        else:
            print(SignUpForm.errors,Register.errors)
    else:
        signup_detail = SignUpForm()
        student_detail = Register()
        hobby = Hobbies()
    return render(request,"registration.html",{'signup_detail':signup_detail,'student_detail':student_detail,"registerd":registered,'hobbies':hobby,'h':True})

def user_login(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                print(request.user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not activated")

        else:
            print("someone tried to login but login failure")
            print("Username: {} Password: {} ".format(username,password))
            return HttpResponse("Invalid Login details")
    else:
        return render(request,"login.html",{})


def profile_page(request):
    user_id = request.user
    u_id = request.user.id
    print(type(user_id))
    try:
        user_details = Student_profile.objects.filter(user=user_id)
        hobbies = Hobby_details.objects.all()
        print(user_details)
    except:
        raise Http404("you are logged out you need to login")
    return render(request, "profile_details.html" , {'user_details':user_details,'hobbies':hobbies})

def edit_student_form(request):
    try:

        n = request.user.id
        if n == 1:
            n = 1
            j = 1
        else:
            j = n
            n = n - 4

        k = User.objects.get(pk = j)
        h = Student_profile.objects.get(pk = n)
        i = Hobby_details.objects.get(pk = 5)
        signup_detail = SignUpForm(request.POST or None, instance = k)
        student_detail = Register(request.POST or None, instance = h)
        hob = Hobbies(request.POST or None, instance = i)
        if student_detail.is_valid() and hob.is_valid():
            student_detail.save()
            hob.save()
            return HttpResponseRedirect(reverse('profile_page'))
    except:
        raise Http404("you are logged out you need to login")
    return render(request,'registration.html',{'signup_detail':signup_detail,'student_detail':student_detail,'hobbies':hob,'h':False})
