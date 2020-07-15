from django.forms import PasswordInput,EmailInput,NumberInput
from django import forms
from app9.models import StudentTable
class Loginform(forms.Form):
    usrname = forms.CharField(max_length=30,label="User Name")
    pas = forms.CharField(widget=forms.PasswordInput, max_length=8,label="Password")
class Courseform(forms.Form):
    coursename = forms.CharField(max_length=30,label="Course Name")
class Studentform(forms.ModelForm):
    class Meta:
        model=StudentTable
        fields="__all__"
        labels={"name":"Name","email":"Email","con":"Contact No","dob":"D.O.B","course":"Course","gen":"Gender",
                "usrname":"UserName","pas":"Password"}
        widgets={"email":EmailInput(),"con":NumberInput(),"pas":PasswordInput()}