from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as dj_login, logout, authenticate
from django.contrib import messages
from .models import student,CustomUser, EnrollCourse



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
    

def view_students(request):

    return render(
        request,
        "main/view_students.html"
        )

def list_students(request):
    all_students = student.objects.all()
    if request.method == "POST":
        search_id = request.POST.get('search_id')
        

    filter_id = student.objects.filter(roll = search_id)

    return render(
        request,
        "main/list_students.html",
        {'all_students': filter_id}
        )



def enroll_course(request):
   

    if request.method == "POST":
        if request.POST.get('dept') and request.POST.get('crs_teacher') and request.POST.get('batch') and request.POST.get('session')  :
            post=EnrollCourse()
            post.teacher= request.POST.get('crs_teacher')
            post.session= request.POST.get('session')
          
            post.dept= request.POST.get('dept')
            post.batch= request.POST.get('batch')

            post.save()
            messages.info(request, f"Data inserted for { request.POST.get('crs_teacher') }")
        else:
            messages.error(request, "Please Fill Up all the Fields")

    return render(
        request,
        "main/enroll_course.html"
        )




def view_enrolled_course(request):
    uniq_dept =  EnrollCourse.objects.values('dept').distinct()
    return render(
        request,
        "main/view_enrolled_course.html",
        {"uniq_dept":uniq_dept}
        )



def fetch_teacher(request):
    all_teachers = CustomUser.objects.all()

    if request.method == "POST":
        selectedDept = request.POST.get('selectedDept')
        

    filter_teacher = CustomUser.objects.filter(dept = selectedDept, userRole = 'teacher')

    return render(
        request,
        "main/fetch_teacher.html",
        {'all_teachers': filter_teacher}
        )


def account(request):
    return render(request,'main/account.html',{'user':request.user})   



def fetch_enrolled_teacher(request):

    if request.method == "POST":
        selectedDept = request.POST.get('selectedDept')
        

    filter_teacher = EnrollCourse.objects.filter(dept = selectedDept).values('teacher').distinct()

    return render(
        request,
        "main/fetch_enrolled_teacher.html",
        {'all_enrolled_teachers': filter_teacher}
        )


def fetch_enrolled_session(request):

    if request.method == "POST":
        crs_teacher = request.POST.get('crs_teacher')
        

    filter_session = EnrollCourse.objects.filter(teacher = crs_teacher).values('session').distinct()

    return render(
        request,
        "main/fetch_enrolled_session.html",
        {'all_enrolled_session': filter_session}
        )


def fetch_enrolled_batch(request):

    if request.method == "POST":
        crs_teacher = request.POST.get('crs_teacher')
        session = request.POST.get('session')
        

    filter_batch = EnrollCourse.objects.filter(teacher = crs_teacher, session = session).values('batch').distinct()

    return render(
        request,
        "main/fetch_enrolled_batch.html",
        {'all_enrolled_batch': filter_batch}
        )

def view_enrolled_student(request):
    if request.method == "POST":
        selectedDept = request.POST.get('dept')
        selectedBatch = request.POST.get('batch')

        filter_student = student.objects.filter(batch = selectedBatch, dept = selectedDept)
        

    return render(request,
        'main/view_enrolled_student.html',
         {'all_enrolled_student': filter_student}
        )   

