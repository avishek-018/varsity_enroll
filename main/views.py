from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as dj_login, logout, authenticate
from django.contrib import messages
from .models import student



# Create your views here.
def homepage(request):
	return render(
			request,
			'main/home.html'
		)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                dj_login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def cpanel(request):
	return render(
		request,
		"main/cpanel.html"
		)

def add_student(request):

    if request.method == "POST":
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('b_date') and request.POST.get('roll') and request.POST.get('dept') and request.POST.get('batch') :
            post=student()
            post.first_name= request.POST.get('first_name')
            post.last_name= request.POST.get('last_name')
            post.b_date= request.POST.get('b_date')
            post.roll= request.POST.get('roll')
            post.dept= request.POST.get('dept')
            post.batch= request.POST.get('batch')

            post.save()
            messages.info(request, f"Data inserted for { request.POST.get('first_name') }")
        else:
            messages.error(request, "Please Fill Up all the Fields")

            
    return render(
        request,
        "main/add_student.html"
        )
<<<<<<< HEAD


def view_students(request):

return render(
    request,
    "main/view_students.html"
    )
=======
>>>>>>> origin/master
    