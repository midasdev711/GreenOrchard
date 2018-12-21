from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Expenses(models.Model):
    name = models.CharField(max_length=100)
    # amount = models.DecimalField() #Needs arguments
    # month = just month here
    # year = just month here
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    # category = foreign key to category
    # bank_id = foreign key to their bank
    # user_id = foreign key to specific user


# class Banks(models.Model):
#     name = models.CharField(max_length=100)
#     abbr = models.CharField(max_length=100)


# class Categories(model.Model):
#     category = model.CharField(max_length=100)


# class Expense_Nicknames(model.Model):
#     nickname = models.CharField(max_length=100)
#     original_expense = models.ForeignKey(Expenses)
