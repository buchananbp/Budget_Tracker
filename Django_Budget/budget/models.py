from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class BankNames(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.name)

class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(BankNames, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.account)
    
# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(BankNames, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

