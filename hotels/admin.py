from django.contrib import admin

from .models import Hotel

#class HotelAdmin(admin.ModelAdmin):
    #list_display = ('hotel_id', 'title', 'address', 'city', 'state', 'zipcode' ,'rating')
    #list_display_links = ('id', 'roomnumber', 'hotel_id',)
    #list_filter = ('id', 'is_occupied', 'hotel_id',)
    #list_editable = ('is_occupied', 'price')
    # search_fields = ('roomnumber')
 


admin.site.register(Hotel)
