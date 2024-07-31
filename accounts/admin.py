from django.contrib import admin
from .models import AccountsModel 


class AccountsModelAdmin(admin.ModelAdmin):
    list_display = ['birth','name','surname','region','phone_number','email','id','is_verified']


admin.site.register(AccountsModel,AccountsModelAdmin)