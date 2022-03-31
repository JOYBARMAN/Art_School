from django.urls import path
from .views import home , StudentView ,DeleteStudentView ,CreateStudentView,EditStudentView,PaymentView
urlpatterns = [
    path('',home,name='home'),
    path('students/',StudentView.as_view(),name="students"),
    path('students/<int:pk>/delete',DeleteStudentView.as_view(),name="delete-student"),
    path('students/add',CreateStudentView.as_view(),name='add-student'),
    path('students/<int:pk>/edit',EditStudentView.as_view(),name='edit-student'),
    path('student/payment',PaymentView.as_view(),name='student-payment')
]