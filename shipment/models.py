from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number =models.CharField(max_length=13)
    address = models.CharField(max_length=500)

class Consignment(models.Model):
    name =models.CharField(max_length=100)
    type =models.CharField(max_length=50)
    year =models.IntegerField()
    isbn =models.IntegerField()
    author =models.CharField(max_length=100)
    genre =models.CharField(max_length=100)
    language =models.CharField(max_length=100)

class AddressDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # shipment = models.ForeignKey(ShipmentDetails,on_delete=models.CASCADE)
    consignment = models.ForeignKey(Consignment,on_delete= models.CASCADE)
    sender_add_line_1 =models.CharField(max_length=100)
    sender_add_line_2 =models.CharField(max_length=100)
    receiver_add_line_1 =models.CharField(max_length=100)
    receiver_add_line_2 =models.CharField(max_length=100)  

class ShipmentDetails(models.Model):
    # user= models.ForeignKey(User,on_delete=models.CASCADE)
    consignment = models.CharField(max_length=100,null=True,blank=True)
    shipment_id = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.CharField(max_length=100,null=True,blank=True)
    shipment_state = models.CharField(max_length=100,null=True,blank=True)
    tracking_url = models.CharField(max_length=500,null=True,blank=True)


class TrackingDetails(models.Model): 
    # user= models.ForeignKey(User,on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100,null=True,blank=True)
    shipment_id = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100,null=True,blank=True)
    origin = models.CharField(max_length=50,null=True,blank=True)
    tracking_page_url = models.CharField(max_length=500,null=True,blank=True)
    destination = models.CharField(max_length=100,null=True,blank=True)
    