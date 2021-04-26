from django.contrib import admin


from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'lname', 'fname','hotel_id','phone', 'email', 'is_eom')
    #list_filter = ('id', 'fname', 'lname')
    #list_editable = ('phone', 'is_eom')
   

admin.site.register(Staff)
