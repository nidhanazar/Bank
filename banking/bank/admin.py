from django.contrib import admin
from .models import User,BankAccountType,UserBankAccount,UserAddress
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email']
admin.site.register(User,UserAdmin)

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['name','maximum_withdrawal_amount']
admin.site.register(BankAccountType,BankAccountAdmin)

class UserBankAdmin(admin.ModelAdmin):
    list_display = ['user','account_type','account_no','gender','birth_date','balance']
admin.site.register(UserBankAccount,UserBankAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user','street_address','city','postal_code','country']
admin.site.register(UserAddress,UserAddressAdmin)

