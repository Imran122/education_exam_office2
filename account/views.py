from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def registration(request):
#     classes_name = Class.objects.all()
#     if request.method == "POST":
#         if request.POST['password'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'student/student_profile/registration.html',{'error': "username has already taken"})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(username = request.POST['username'],email = request.POST['email'],password=request.POST['password'])
#                 name = request.POST.get('name')
#                 # age = request.POST.get('age')
#                 # group = request.POST.get('group')
#                 # profile_picture = request.FILES.get('profile_picture')
#                 # cover_picture = request.FILES.get('cover_picture')
#                 # phone = request.POST.get('phone')
#                 # address= request.POST.get('address')
#                 # pk_id = request.POST.get('classes_name')
#                 # classes_name = request.objects.get(pk_id=pk_id)
#                 # print(pk_id)
#                 # print(classes_name)
#                 profile = Student(name=name, user=user)
#                 profile.save()
#                 return redirect(reverse_lazy('registration'))
#         else:
            
#             return render(request, 'student/student_profile/registration.html')
#     else:
#         context ={
#             'classes_name':classes_name,
#         }
        return render(request, 'account/registration.html')


def login(request):
      return render(request, 'account/login.html')