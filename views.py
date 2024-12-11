from django.shortcuts import render
from app1.models import marks2 



# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response 
def add_student_template(request):
    response=render(request,"app1/add_student.html")
    return response
def add_student(request):
    rono=int(request.GET['rono'])
    name=request.GET['name']
    s1=float(request.GET['sub1'])
    s2=float(request.GET['sub2'])
    m=marks2(rono=rono,name=name,sub1=s1,sub2=s2)
    m.save()
    response=render(request,"app1/add_student.html",context={'msg':'Student Added'})
    return response
def updatemarks_template(request):
    response=render(request,"app1/update_student.html")
    return response
def updatemarks(request):
    rollno=int(request.GET["ro"])
    s1=float(request.GET['sub1'])
    s2=float(request.GET['sub2'])
    try:
        stud=marks2.objects.get(rono=rollno)
        stud.sub1=s1
        stud.sub2=s2
        stud.save()
        response=render(request,"app1/update_student.html",context={'msg':"Marks updated"})
    except:
        response=render(request,"app1/update_student.html",context={"msg":"inalid roll no"})
    return response
def delete_template(request):
    response=render(request,"app1/delete_student.html")
    return response
def delete(request):
    rollno=int(request.GET['Rollno'])
    try:
        rono=marks2.objects.get(rono=rollno)
        rono.delete()
        response=render(request,"app1/delete_student.html",context={"msg":"deleted record succesfully"})
        return response
    except:
        response=render(request,"app1/delete_student.html",context={"msg":"not match the roll numer"})
        return response
def find_temp(request):
    response=render(request,"app1/find_result.html")
    return response
def find(request):
    rollno=int(request.GET['Rollno'])
    try:
        rono=marks2.objects.get(rono=rollno)
        msg=[rono.rono,rono.name,rono.sub1,rono.sub2]
        response=render(request,"app1/find_result.html",context={"msg":msg})
        return response
    except:
        response=render(request,"app1/find_result.html",context={"msg":"result not found"})
        return response
def view_temp(request):
    qs=marks2.objects.all()
    response=render(request,"app1/views.html",context={"msg":qs})
    return response


    