from typing import Any
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


from django.utils import timezone

from main.customModelManager import PurchaseModelManager
from main.helperMethod import action_on_delete_puchase
# Create a model for product quantity measurements


class WholeSaler(models.Model):
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    mobile_number = PhoneNumberField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    # address = 
    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    convertTo = models.ForeignKey('self',null=True,blank=True,default=None,on_delete=models.SET(None))
    convertNumber = models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):  
        return self.name

# Create a model for the product type

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='brand_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent_type = models.ForeignKey('self',on_delete=models.SET_DEFAULT, null=True, blank=True,default=-1)

    def __str__(self):
        return self.name
# class ProductTypeQuantity(models.Model):
#     product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
#     quantity_measurement = models.ForeignKey(Unit, on_delete=models.CASCADE)
#     value = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.product_type} - {self.quantity_measurement}: {self.value}"

class ProductAttribute(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
        # your_app/static/your_app/js/custom_admin.js
    def __str__(self):
        return f'{self.key}:{self.value}'



class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attributes = models.ManyToManyField(ProductAttribute)
    class Media:
        js = ('admin/js/custom.js',)
    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(Unit,blank=False,null=False,on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_unit = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    whole_saler = models.ForeignKey(WholeSaler, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.number_of_unit} - {self.product} {self.unit_price*self.number_of_unit} - {self.date}"

    def save(self, *args, **kwargs):

        pro_base_quan = self.number_of_unit * self.unit_type.convertNumber
        print(pro_base_quan)
        convertTo = self.unit_type.convertTo
        pro_base_quan = pro_base_quan 
        while convertTo :
            pro_base_quan = pro_base_quan * convertTo.convertNumber
            print(convertTo,convertTo.convertNumber,pro_base_quan)
            convertTo = convertTo.convertTo
        self.product.quantity += pro_base_quan
        print(self.product.quantity)
        self.product.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        action_on_delete_puchase(self)
        super().delete(*args, **kwargs)

class Client(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    AGE_GROUP_CHOICES = [
        ('0-10', '0-10 years'),
        ('10-20', '10-20 years'),
        ('20-40', '20-40 years'),
        ('40-100', '40-100 years'),
    ]


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES, blank=True, null=True)

    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # postal_code = models.CharField(max_length=10)
    # country = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ClientTransaction(models.Model):
    TRANSACTION_CHOICES = [
        ('sale', 'Sale'),
        ('return', 'Return'),
        ('exchange', 'Exchange'),
    ]
    DISCOUNT_CHOICES = [
        ('percent', 'Percentage'),
        ('amount', 'Amount'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=8, choices=TRANSACTION_CHOICES)
    transaction_date = models.DateField()
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=8, choices=DISCOUNT_CHOICES, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

        # Product-related fields
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)

    # New fields


    def __str__(self):
        return f"{self.get_transaction_type_display()} for {self.client} on {self.transaction_date}"
