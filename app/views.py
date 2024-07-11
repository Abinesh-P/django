from django.shortcuts import render
from django.http import HttpRequest
from .models import Contact


# Create your views here.


def index(request):

    return render(request,"index.html")

def contact(request):
    if request.method == 'POST':
        #  Save the form data to the database
        full_name=request.POST['full_name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        birth_date=request.POST['birth_date']
        gender=request.POST['gender']
        street_address=request.POST['street_address']
        city=request.POST['city']
        region=request.POST['region']
        postal_code=request.POST['postal_code']
        country=request.POST['country']
        obj = Contact()
        obj.full_name=full_name
        obj.email=email
        obj.phone_number=phone_number
        obj.birth_date=birth_date
        obj.gender=gender
        obj.street_address=street_address
        obj.city=city
        obj.region=region
        obj.postal_code=postal_code
        obj.country=country
        obj.save()
        mydata=Contact.objects.all()
        return render(request, 'view.html',{'data':mydata}) # Redirect to a success page
    
    
    return render(request, 'contact.html')