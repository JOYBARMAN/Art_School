from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student,Payment
from django.urls import reverse_lazy
from .forms import StudentForm, StudentUpdateForm ,StudentPaymentForm


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

class CreatePayment(CreateView):
    model = Payment
    form_class = StudentPaymentForm
    template_name = "student_payment_add.html"
    success_url = reverse_lazy("student-payment")