from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'roomnumber', 'hotel_id','title', 'is_occupied', 'price', 'beds', 'date_in' ,'date_out')
    list_display_links = ('id', 'roomnumber', 'hotel_id',)
    list_filter = ('id', 'is_occupied', 'hotel_id',)
    list_editable = ('is_occupied', 'price')
    # search_fields = ('roomnumber')
 
admin.site.register(Listing, ListingAdmin)
