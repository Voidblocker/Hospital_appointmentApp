from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import Appointment
from .models import User
from django.contrib import messages

# Create your views here.
def home_view(request):
    form = Appointment(request.POST or None)
    context={
        "input": form
    }
    if request.method == 'POST':
        if form.is_valid():
            # User.objects.create(First_name=form.cleaned_data['First_name'],Last_name=form.cleaned_data['Last_name']
            #                     ,email=form.cleaned_data['email'], phone_number=form.cleaned_data['phone_number'],
            #                     date=form.cleaned_data['date'], preference=form.cleaned_data['preference'])
            form.save()
            return redirect('created')
        else:
            return messages.error(request, 'Enter the correct fields')
    return render(request , "appointment_app/index.html", context)

def blog_detail(request):
    return render( request , "appointment_app/blog-details.html")
