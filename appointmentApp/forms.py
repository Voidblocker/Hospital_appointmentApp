from django import forms 
from .models import User

class Appointment(forms.ModelForm):

    class Meta:
        model = User
        fields = ("First_name" ,"Last_name" , "email", "phone_number","date", "preference")
        widgets={
            "First_name" : forms.TextInput(attrs={ "class":"form-control", "id":"name", "name":"name", "placeholder":"First Name"}),
            "Last_name" : forms.TextInput(attrs={ "class":"form-control", "id":"name", "name":"name", "placeholder":"Last Name"}),
            "email" : forms.TextInput(attrs={ "class":"form-control", "id":"email", "name":"email", "placeholder":"Email"}),
            "phone_number" : forms.TextInput(attrs={ "class":"form-control", "id":"mobile", "name":"mobile", "placeholder":"Mobile Number"}),
            "date" : forms.DateInput(attrs={"class":"form-control", "id":"datepicker", "name":"date-form", "placeholder":"Form"}),
            "preference" : forms.Select(attrs={"type":"radio","class":"btn btn-primary", "name":"options", "id":"option1", }) 
        }
