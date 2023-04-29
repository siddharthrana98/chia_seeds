from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone  
from django.contrib.auth.models import User
# Create your models here.


################### OFFERCARD#######################################
class Offercard(models.Model):
    # productid=models.ForeignKey(to=Product,on_delete=models.CASCADE)
    productid=models.CharField(max_length=20)
    from_date=models.DateTimeField(default=timezone.now)
    to_date=models.DateTimeField(default=timezone.now)
    discount=models.IntegerField(blank=True)
    status=models.CharField(max_length=20, default="True")
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(default=timezone.now)

###################### product##################################################
class Product(models.Model):
    userid=models.ForeignKey(to=User,on_delete=models.CASCADE)
    # categoryid=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    userid=models.CharField(max_length=200, default="")
    productname=models.CharField(max_length=200, default="")
    productdescription=models.CharField(max_length=300, default="")
    productimages=models.ImageField(upload_to="api_app/img", blank=True)
    productThumbnail=models.ImageField(upload_to="api_app/img", blank=True)
    productprice=models.IntegerField(blank=True)

    productdiscountPercentage=models.IntegerField(blank=True)
    productdiscountPrice=models.IntegerField(blank=True)
    productfinalPrice=models.IntegerField(blank=True,null=True)
    gsttax = models.IntegerField(blank=True)

    productqty=models.IntegerField(blank=True)
    productmetaTitle=models.CharField(max_length=200, default="")
    status=models.CharField(max_length=20, default="True")
    createdate=models.DateTimeField(default=timezone.now)
    updatedate=models.DateTimeField(auto_now=True)

########################### PRODUCT REVIEW ######################################

class ProductReview(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    product_name=models.ForeignKey(to=Product,on_delete=models.CASCADE)
    user=models.CharField(max_length=200, default="")
    product_name=models.CharField(max_length=200, default="")

    reviewDescription=models.CharField(max_length=500, default="")
    reviewTitle=models.CharField(max_length=200, default="")
    reviewRating=models.IntegerField()
    reviewImage=models.ImageField(upload_to="api_app/img", default="")
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(default=timezone.now)

class UserCart(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    product=models.ForeignKey(to=Product,on_delete=models.CASCADE)
    orderQty=models.IntegerField()
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(default=timezone.now)

class Order(models.Model):
    # ProductStockId=models.ForeignKey(to=ProductStock,on_delete=models.CASCADE)
    orderId = models.CharField(max_length=200, default="")
    orderQty=models.IntegerField()
    tranctionNumber = models.IntegerField()
    deliveryCharge = models.IntegerField()
    orderstatus= models.CharField(max_length=50, default="")
    paymentMethod = models.CharField(max_length=200, default="")
    tranctionId = models.CharField(max_length=200, default="")
    shipingInfo= models.CharField(max_length=300, default="")
    billingInfo= models.CharField(max_length=300, default="")
    paymentstatus=models.CharField(max_length=50, default="")
    orderComment=models.CharField(max_length=500, default="")
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(default=timezone.now)