from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse

from teacher.models import Teacher
from student.models import Student
from .models import BaseUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import Error, IntegrityError

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("redirect")
    elif request.method == "POST":
        login_email = request.POST.get("login-email")
        login_password = request.POST.get("login-password")
        user = authenticate(request, email=login_email, password=login_password)
        if user is not None:
            login(request, user)
            if user.user_type == "TEACHER":
                return redirect("/psc_dashboard")
            elif user.user_type == "SUPERUSER":
                return redirect("/admin")
            elif user.user_type == "STUDENT":
                return redirect("/comm_dashboard")
            else:
                return HttpResponse("Please contact admin.")
        else:
            messages.error(request, "Login Credentials Failed. Check your email and password.")
            return redirect("/login")
    else:
        content_parser = {'title': 'Login- Connectio'}
        return render(request, "login1.html", content_parser)

def registration_teacher(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user_type = "TEACHER"
            Teacher.objects.create(
                name=request.POST.get("name"),
                email=email,
                organization=request.POST.get("org"),
                country=request.POST.get("country"),
                # organization_type=request.POST.get("org_type"),
                state=request.POST.get("stt"),
                mobile=request.POST.get("mobile"),
                city=request.POST.get("city"),
                designation=request.POST.get("desig"),
                # linked_in=request.POST.get("linkedin"),
                # department=request.POST.get("dept"),
                idproof=request.FILES.get("nomination"),
            )
            BaseUser.objects.create_user(email=email, password=password, user_type=user_type)
            messages.success(request, "Account Created Successfully.")
            return redirect('login')
        except IntegrityError as e:
            print(e)
            messages.error(request, "The email might have been used already. If you haven't registered with us, "
                                    "retry with the same email or try with a different email.")
        except Error:
            messages.error(request, "Something went wrong. Contact admin or try again later.")

    content_parser = {'title': 'Register - Smart India Hackathon 2022'}
    return render(request, "registrationteacher.html", content_parser)

def registration_student(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user_type = "STUDENT"
            Student.objects.create(
                name=request.POST.get("name"),
                email=email,
                mobile=request.POST.get("mobile"),              
            )
            BaseUser.objects.create_user(email=email, password=password, user_type=user_type)
            messages.success(request, "Account Created Successfully.")
            return redirect('login')
        except IntegrityError as e:
            print(e)
            messages.error(request, "The email might have been used already. If you haven't registered with us, "
                                    "retry with the same email or try with a different email.")
        except Error:
            messages.error(request, "Something went wrong. Contact admin or try again later.")

    content_parser = {'title': 'Register - Smart India Hackathon 2022'}
    return render(request, "registrationteacher.html", content_parser)



