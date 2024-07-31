from django.contrib import admin
from .models import TestModel,TestCollectionModel,DTMTestModel

class TestModelAdmin(admin.ModelAdmin):
    list_display = ['code','question','id','image']

class TestCollectionModelAdmin(admin.ModelAdmin):
    list_display = ['subject','code','is_free','id']

class DTMTestModelAdmin(admin.ModelAdmin):
    list_display = ['code','id']


admin.site.register(DTMTestModel,DTMTestModelAdmin)
admin.site.register(TestCollectionModel,TestCollectionModelAdmin)
admin.site.register(TestModel,TestModelAdmin)


