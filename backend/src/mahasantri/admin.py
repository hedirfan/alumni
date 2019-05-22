from django.contrib import admin
from .models import Identita

class MahasantriAdmin(admin.ModelAdmin):
    list_display=('username','password','email','fullname', 'address','phone_number','year','job')

admin.site.register(Identita, MahasantriAdmin)