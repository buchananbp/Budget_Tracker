from django.contrib import admin
from .models import Transaction, Category, Bank, BankNames

admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Bank)
admin.site.register(BankNames)

