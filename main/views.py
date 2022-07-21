from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Student,Payment
from django.urls import reverse_lazy
from .forms import StudentForm, StudentUpdateForm ,StudentPaymentForm,StudentPaymentUpdateForm ,NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


class StudentView(ListView):
    model = Student
    template_name = 'student.html'
    ordering = ['roll']


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'student-delete.html'
    success_url = reverse_lazy('students')


class CreateStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student-add.html"
    success_url = reverse_lazy("students")


class EditStudentView(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'edit-student.html'
    success_url = reverse_lazy("students")


class PaymentView(ListView):
    model = Payment
    template_name = 'student_payment.html'
    ordering = ['student']

class CreatePaymentView(CreateView):
    model = Payment
    form_class = StudentPaymentForm
    template_name = "student_payment_add.html"
    success_url = reverse_lazy("student-payment")


class EditPaymentView(UpdateView):
    model = Payment
    form_class = StudentPaymentUpdateForm
    template_name = 'edit-student-payment.html'
    success_url = reverse_lazy("student-payment")


class DeletePaymentView(DeleteView):
    model = Payment
    template_name = "student_payment_delete.html"
    success_url = reverse_lazy("student-payment")


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("home")


def contactUs(request):
    return render(request, 'contactUs.html')