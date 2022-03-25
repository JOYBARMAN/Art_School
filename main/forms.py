from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','roll','group','email','gender','mobile','photo','blood','address','father_name','mother_name','admission_date')

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','roll','group','email','gender','mobile','photo','blood','address','father_name','mother_name','admission_date')
