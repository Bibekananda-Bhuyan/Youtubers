from django import forms
from . models import *
import random,string,datetime
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Create Unique Id

def unque_id_generator():
    ts = datetime.datetime.now().timestamp()
    ts = str(ts)
    ts = ts.split(".")
    ts=ts[0]
    ran=random.randint(1,100)
    ran=str(ran)
    uid=ts+ran
    return uid

class Creatorregistationform(forms.ModelForm):
    creator_first_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"id":"materialRegisterFormFirstName","class":"form-control"}),required=True,error_messages={"required":"Please Enter Your First Name"})
    creator_last_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"id":"materialRegisterFormLastName","class":"form-control"}),required=True)
    creator_email=forms.EmailField(max_length=500,widget=forms.TextInput(attrs={"id":"materialRegisterFormEmail","class":"form-control"}),required=True)
    creator_password=forms.CharField(max_length=500,widget=forms.PasswordInput(attrs={"id":"materialRegisterFormPassword","class":"form-control"}),required=True)
    creator_phoneno=forms.CharField(max_length=10,widget=forms.NumberInput(attrs={"id":"materialRegisterFormPhone","class":"form-control"}),required=True)
    creator_platform=forms.ModelChoiceField(queryset=Platform.objects.all())
    email_verificationid=forms.CharField(max_length=300,widget=forms.HiddenInput(attrs={"value":randomString(50)}))
    unquie_id = forms.CharField(max_length=300, widget=forms.HiddenInput(attrs={"value": unque_id_generator()}))

    class Meta:
        model=Creator
        fields=["creator_first_name","creator_last_name","creator_email","creator_password","creator_phoneno","creator_platform","email_verificationid","unquie_id"]





class Brand_Signupform(forms.ModelForm):
    brand_name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={"id": "materialRegisterFormFirstName", "class": "form-control"}), required=True,
                                         error_messages={"required": "Please Enter Your First Name"})

    brand_email = forms.EmailField(max_length=500, widget=forms.TextInput(
        attrs={"id": "materialRegisterFormEmail", "class": "form-control"}), required=True)
    brand_password = forms.CharField(max_length=500, widget=forms.PasswordInput(
        attrs={"id": "materialRegisterFormPassword", "class": "form-control"}), required=True)
    brand_phoneno = forms.CharField(max_length=10, widget=forms.NumberInput(
        attrs={"id": "materialRegisterFormPhone", "class": "form-control"}), required=True)
    unquie_id = forms.CharField(max_length=300, widget=forms.HiddenInput(attrs={"value": unque_id_generator()}))
    email_verificationid = forms.CharField(max_length=300, widget=forms.HiddenInput(attrs={"value": randomString(50)}))

    class Meta:
        model=Brand
        fields=["brand_name","brand_email","brand_password","brand_phoneno","email_verificationid","unquie_id"]




class Creator_loginform(forms.ModelForm):
    creator_email = forms.EmailField(max_length=500, widget=forms.TextInput(
        attrs={"id": "materialRegisterFormEmail", "class": "form-control"}), required=True)
    creator_password = forms.CharField(max_length=500, widget=forms.PasswordInput(
        attrs={"id": "materialRegisterFormPassword", "class": "form-control"}), required=True)
    class Meta:
        model=Creator
        fields=["creator_email","creator_password"]


class Brand_loginform(forms.ModelForm):
    brand_email = forms.EmailField(max_length=500, widget=forms.TextInput(
        attrs={"id": "materialRegisterFormEmail", "class": "form-control"}), required=True)
    brand_password = forms.CharField(max_length=500, widget=forms.PasswordInput(
        attrs={"id": "materialRegisterFormPassword", "class": "form-control"}), required=True)
    class Meta:
        model=Creator
        fields=["brand_email","brand_password"]




