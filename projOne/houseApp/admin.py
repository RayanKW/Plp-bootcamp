from django.contrib import admin
from .models import houseListingModel

# Register your models here.
@admin.register(houseListingModel) #the decorator and the list_display customizes the admin site to show all the fields
# admin.site.register(houseListingModel)
class houseListingAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'noBedrooms', 'squareField'
    )
    # list_editable = (
    #     'title', 'noBedrooms', 'squareField'
    # )
    # # prepopulated_fields = {'id':('title')}
    # list_per_page = 5
