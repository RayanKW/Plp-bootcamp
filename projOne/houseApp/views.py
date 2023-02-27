from django.shortcuts import render
from .models import houseListingModel
# Create your views here.
"""
listing
CRUD - Create, Read, Update, Delete, listiing all elements

"""
def house_listings(request):
    listings = houseListingModel.objects.all()#a querrry to select our houses listed and store it in listing
    context = {
        'list': listings,
        #you can add another key here
    }
    return render(request, 'listings.html', context)# render returns request, , and a context. The context is a diectionary
#remove the context and replace with {} and use h1 tages in the listing...why does it display the h1 but li it doesnt
def retrDetails(request, pk):
    specific_house = houseListingModel.objects.get(id=pk)
    context = {
        'spec': specific_house #the value in the context is the variable
    }
    return render(request, 'details.html', context)