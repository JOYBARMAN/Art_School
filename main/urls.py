from django.urls import path
from .views import home, StudentView, DeleteStudentView, CreateStudentView, EditStudentView, PaymentView,\
    CreatePaymentView, EditPaymentView, DeletePaymentView ,register_request,login_request,logout_request,ContactView

urlpatterns = [
    path('', home, name='home'),
    path('students/', StudentView.as_view(), name="students"),
    path('students/<int:pk>/delete', DeleteStudentView.as_view(), name="delete-student"),
    path('students/add', CreateStudentView.as_view(), name='add-student'),
    path('students/<int:pk>/edit', EditStudentView.as_view(), name='edit-student'),
    path('student/payment', PaymentView.as_view(), name='student-payment'),
    path('student/payment/add', CreatePaymentView.as_view(), name='add-student-payment'),
    path('student/payment/<int:pk>/edit', EditPaymentView.as_view(), name='edit-student-payment'),
    path('student/payment/<int:pk>/delete', DeletePaymentView.as_view(), name='delete-student-payment'),
    path("contact/",ContactView.as_view(), name="contact"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout", logout_request, name="logout"),
]
