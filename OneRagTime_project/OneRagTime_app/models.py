from django.db import models

# Create your models here.
class Investments(models.Model):
    investor_id = models.IntegerField()
    startup_name = models.CharField(max_length=255)
    invested_amount = models.IntegerField()
    percentage_fees = models.IntegerField()
    date_added = models.DateField(auto_created=True)
    fees_type = models.CharField(max_length=255)

class Investor(models.Model):
    name= models.CharField(max_length=255)
    adress= models.CharField(max_length=255)
    credit= models.CharField(max_length=255)
    phone= models.CharField(max_length=255)
    email= models.CharField(max_length=255)

class Bill(models.Model):
    investor_id = models.IntegerField()
    investment_id = models.IntegerField()
    fees_amount = models.IntegerField()
    date_added = models.DateField()
    fees_type = models.CharField(max_length=255)

class Cashcall(models.Model):
    total_amount = models.IntegerField()
    IBAN = models.IntegerField()
    email_send = models.CharField(max_length=255)
    date_added = models.DateField()
    invoice_status = models.CharField(max_length=255)