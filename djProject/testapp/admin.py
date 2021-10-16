from django.contrib import admin
from testapp.models import *

# Register your models here.
class delhijobsAdmin(admin.ModelAdmin):
	list_display= ['date','company', 'title', 'eligibility', 'address', 'email','phonenumber']

class hydjobsAdmin(admin.ModelAdmin):
	list_display= ['date','company', 'title', 'eligibility', 'address', 'email','phonenumber']

class mumbaijobsAdmin(admin.ModelAdmin):
	list_display= ['date','company', 'title', 'eligibility', 'address', 'email','phonenumber']
admin.site.register(deljobs,delhijobsAdmin)
admin.site.register(hyjobs,hydjobsAdmin)
admin.site.register(mumjobs,mumbaijobsAdmin)



