from django.shortcuts import render
from .models import houseListingModel
# Create your views here.
"""
listing
CRUD - Create, Read, Update, Delete

"""
def house_listings(request):
    listings = houseListingModel.objects.all()#a querrry to select our houses listed
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', {})# render returns request, , and a context. The context is a diectionary
