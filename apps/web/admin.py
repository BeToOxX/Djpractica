from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class resourcePetshop (resources.ModelResource):
    class Meta:
        model = petshop

class adminPetshop(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'direction', 'phone', 'owner']
    resource_class = resourcePetshop

admin.site.register(petshop, adminPetshop)

class resourcePet (resources.ModelResource):
    class Meta:
        model = pet

class adminPet(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','race', 'gender', 'description', 'age']
    resource_class = resourcePetshop

admin.site.register(pet, adminPet)

class resourceCita(resources.ModelResource):
    class Meta:
        model = cita

class adminCita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_cita']
    list_display = ['fecha', 'fk_pet', 'fk_petshop']
    resource_class = resourceCita

admin.site.register(cita, adminCita)
