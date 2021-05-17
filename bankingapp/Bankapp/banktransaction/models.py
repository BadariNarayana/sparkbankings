from django.db import models
from django.utils import timezone
# Create your models here.

class AccountsModels(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    dateOfBirth = models.DateField()
    balance = models.IntegerField()
    accountNumbers = models.CharField(max_length = 5,default=' ')
    def _str_(self):
        return self.firstName+" "+self.lastName
        
class TransactionTable(models.Model):
    TransactionId = models.CharField(max_length=10)
    FromAccNo = models.CharField(max_length=5)
    ToAccNo = models.CharField(max_length=5)
    Amount = models.IntegerField()
    dateTime = models.DateField(default=timezone.now)

    def _str_(self):
        return self.TransactionId