from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department_id = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=200, null = True)
    serial_no = models.CharField(max_length=200, null = True)
    description = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved','Approved'),
        ('Out','Out'),
        ('Servicing','Servicing'),
    )
    #customer = models.CharField(max_length=200, null = True)
    #item = models.CharField(max_length=200, null = True)
    cname = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    item_name = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f"Order by {self.cname} for {self.iname}"
    

    

