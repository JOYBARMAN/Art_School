from django import forms
from .models import Student,Payment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','roll','group','email','gender','mobile','photo','blood','address','father_name','mother_name','admission_date')

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','roll','group','email','gender','mobile','photo','blood','address','father_name','mother_name','admission_date')

class StudentPaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=('__all__')

class StudentPaymentUpdateForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=('__all__')

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username", "email", "password1", "password2")

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user