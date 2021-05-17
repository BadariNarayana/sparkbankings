from django.contrib import admin
from .models import AccountsModels, TransactionTable
# Register your models here.

admin.site.register(AccountsModels)
admin.site.register(TransactionTable)
