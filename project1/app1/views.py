from django.shortcuts import render,redirect
from app1.models import Student
from django.views import View
from django.http import HttpResponse
# Create your views here.
class HomeView(View):
    def get(self,request):
        students=Student.objects.all()
        return render(request,'index.html',{'students':students})

class StudentRegister(View):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        print(request.POST)  # {name:"anu","place":"calicut"}
        name=request.POST.get("name")
        place=request.POST.get("place")
        age=request.POST.get("age")
        email=request.POST.get("email")
        print(name,age,place,email)
        Student.objects.create(name=name,place=place,age=age,email=email)
        return redirect('home_view')

class DeleteStudent(View):
    def get(self,request,**kwargs):  
        stud_id=kwargs.get("id")
        student=Student.objects.get(id=stud_id)  
        student.delete()
        return redirect("home_view")

       
