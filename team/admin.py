from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Kid)
class KidAdmin(admin.ModelAdmin):
	list_display = ['name', 'last_name', 'team']

@admin.register(models.Leader)
class LeaderAdmin(admin.ModelAdmin):
	list_display = ['name', 'school']

admin.site.register(models.Team)
admin.site.register(models.Bitacora)
#admin.site.register(models.Kid)
#admin.site.register(models.Responsable)