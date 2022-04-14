from django.shortcuts import render
from ContactUs.forms import ContactForm
from ContactUs.models import ContactUs
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def formgiven(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            details=form.cleaned_data['details']

            Contactobj=ContactUs.objects.create(
                name=name,
                email=email,
                details=details,
            )

            Contactobj.save()
            messages.success(request, 'Data Submitted Succesfully!')
        else:
            messages.error(request, 'Invalid Request, Please fill the form properly!')
    else:
        form = ContactForm()
    context={
        'form':form,
    }
    return render(request,'form.html',context)

def fetchdata(request):
    data=ContactUs.objects.all().order_by('id')
    context={
        'data':data,
    }
    return render(request,'data.html',context)