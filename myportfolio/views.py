from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Project,WorkExperience,Education,Post



# Create your views here.
def index(request):
     context = {
          "title":"Home"
     }
     return render(request, "index.html", context)

def cv(request):
     educations = Education.objects.all()
     works = WorkExperience.objects.all()
     context = {
          "title":"cv",
          "works" : works,
          "educations":educations
     }
     return render(request, "cv.html", context)


def hire(request):
     context = {
          "title":"Hire",
          
     }
     if request.method == "POST":
          
               name = request.POST['name']
               message = request.POST['message']
               phone_number = request.POST['phone_number']
               subject = request.POST['subject']           
               email = request.POST['email']
               date = request.POST['date']

               # if Post.objects.filter(name=name).exists():
               #       messages.info(request, 'Email already exits')
               #       return redirect ('hire')
               # elif Post.objects.filter(email=email).exists():
               #       messages.info(request, 'Email already exits')
               #       return redirect('hire')
               # else:
               user=Post.objects.create(
                           name=name,email=email,message=message, phone_number=phone_number,date=date)
               user.save()
               return redirect('cv')         
              
     else:
           return render(request, "hire-me.html",context)

def projects(request):
     projects = Project.objects.all()
     context = {
          "title":"Projects",
          "projects":projects
     }
     return render(request, "projects.html",context)

