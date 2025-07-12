from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User,Group
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    customer_email = models.EmailField(unique=True)
    customer_password = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=15)
    customer_address = models.TextField()


    def __str__(self):
         return f"{self.customer_name}"
    
class Restaurant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    restaurant_email = models.EmailField(unique=True)
    restaurant_address = models.TextField()
    restaurant_phone_number = models.CharField(max_length=15)
    

    def __str__(self):
         return f"{self.restaurant_name}"

class MenuItem(models.Model):
    menu_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='menu_items')
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image=models.ImageField(upload_to='foodimages/',default=None,blank=True)
    def __str__(self):
         return f"{self.item_name}"

class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    driver_email = models.EmailField(unique=True)
    driver_phone_number = models.CharField(max_length=15)
    driver_current_location = models.CharField(max_length=100)

    def __str__(self):
         return f"{self.user}"

class Order(models.Model):

    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    items = models.ManyToManyField(MenuItem)
    date=models.DateTimeField(null=True,blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.order_id}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date=models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
         return f"{self.method}"


class Rating(models.Model):
    rating_id=models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    stars = models.IntegerField()  
    def __str__(self):
         return f"{self.stars}"
