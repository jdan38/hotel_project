from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    pass
    #list_display = ('id','roomnumber', 'hotel_id','title', 'is_occupied', 'price', 'beds')
    #list_display_links = ('roomnumber', 'hotel_id',)
    #list_filter = ('id', 'is_occupied', 'hotel_id',)
    #list_editable = ('is_occupied', 'price')
    # search_fields = ('roomnumber')
 
admin.site.register(Listing, ListingAdmin)
