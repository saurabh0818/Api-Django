from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('payment/', views.PaymentList.as_view()),
    path('studentdetails/<str:pk>/', views.studentdetails, name="studentdetails"),
    path('studentadd/', views.studentadd, name='studentadd'),
    path('studentupdated/<str:pk>/', views.studentupdated, name="studentupdated"),
    path('studentdelete/<str:pk>/', views.studentdelete, name="studentdelete"),
]
