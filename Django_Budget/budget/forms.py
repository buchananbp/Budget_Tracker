from django.forms import ModelForm
from .models import Transaction, Bank, BankNames

class transactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class addPayForm(ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
