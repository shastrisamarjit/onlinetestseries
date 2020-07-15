from django.shortcuts import render,redirect
from app9.models import CourseTable,StudentTable,LoginTable
from django.contrib import messages
from app9.forms import Loginform,Courseform,Studentform
from django.core.paginator import Paginator
def show(request):
    return render(request,'testseries2.html')
def showregister(request):
    x = Studentform()
    return render(request,'registerpage.html',{"data":CourseTable.objects.all(),"student":x})
def showadmin(request):
    return render(request,'adminlogin.html',{"Login":Loginform()})
def showfaculty(request):
    return render(request,'facultypanel.html',{"course":Courseform()})
def savecourse(request):
    x=request.POST.get("coursename")
    CourseTable(coursename=x).save()
    messages.success(request, "Course Saved")
    return redirect("facultypanel")
def saveregister(request):
    x=request.POST.get("usrname")
    y=request.POST.get("pas")
    ty="student"
    LoginTable(usrname=x,pas=y,type=ty).save()
    st=Studentform(request.POST)
    if st.is_valid():
        st.save()
        messages.success(request,"Registered Successfully")
        return redirect("registerpage")
    else:
        return render(request,"registerpage.html",{"student":st})
def checklogin(request):
    x=request.POST.get("l1")
    y=request.POST.get("l2")
    ty = 'student'
    try:
        LoginTable.objects.get(usrname=x, pas=y,type=ty)
        request.session["status"]=True
        return render(request, "loginpage.html",{"data":StudentTable.objects.filter(usrname=x)})
    except LoginTable.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect('main')
def adminlogin(request):
    x=request.POST.get("usrname")
    y=request.POST.get("pas")
    ty="Admin"
    try:
        LoginTable.objects.get(usrname=x, pas=y, type=ty)
        return render(request, "adminpage.html",{"name": x})
    except LoginTable.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect("adminpage")
def adminpanel(request):
    return render(request,"admindetails.html",{"data":StudentTable.objects.all()})
def showadminpage(request):
    return render(request,"adminpage.html")
def viewall(request):
    student_data=StudentTable.objects.all()
    p=Paginator(student_data,2)
    page_no=request.GET.get("pno")
    if page_no:
        page=p.page(page_no)
    else:
        page=p.page(1)
    return render(request,"viewall.html",{"data":page})
def deletestudent(request):
    return render(request,"deletest.html")
def coursedelete(request):
    return render(request,"coursedelete.html")
def removed(request):
    x=request.POST.get("d1")
    try:
        StudentTable.objects.get(usrname=x)
        StudentTable.objects.filter(usrname=x).delete()
        LoginTable.objects.filter(usrname=x).delete()
        messages.success(request,"Deleted Successfully")
        return redirect("deletestudent")
    except StudentTable.DoesNotExist:
        messages.error(request,"Username Is Invalid")
        return redirect("deletestudent")
def logout(request):
    request.session["status"]=False
    return redirect("main")