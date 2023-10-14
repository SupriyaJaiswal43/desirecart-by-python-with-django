from django.db import models

# Create your models here.

class subcategory(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=70)
    date=models.DateField()
    def __str__(self):
        return self.name


#second table for product details

class product(models.Model):
    id=models.AutoField
    category=models.CharField(max_length=30)
    subcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=110)
    price=models.FloatField()
    disprice=models.FloatField()
    size=models.CharField(max_length=15)
    color=models.CharField(max_length=35)
    description=models.CharField(max_length=350)
    ppic=models.ImageField(upload_to="static/images/",default="");
    date=models.DateField()
    def __str__(self):
        return self.name

class contactinfo(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=100)
    mobno=models.CharField(max_length=20)
    msg=models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class feedbackinfo(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=70)
    img=models.ImageField(upload_to="static/upload/testimonial/",default="");
    state=models.CharField(max_length=100)
    msg=models.CharField(max_length=2000)
    def __str__(self):
        return self.name



class order(models.Model):
    order=id=models.AutoField
    pid=models.IntegerField()
    userid=models.CharField(max_length=50)
    remarks=models.TextField(max_length=1000)
    status=models.BooleanField()
    odate=models.DateField()
def __str__(self):
    return self.userid

class addtocart(models.Model):
    cid=models.AutoField
    pid=models.IntegerField()
    userid=models.CharField(max_length=50)
    status=models.BooleanField()
    odate=models.DateField()
def __str__(self):
    return self.userid

class signup(models.Model):

    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    email=models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
    userpic=models.ImageField(upload_to='static/profile/',null=True)
    address = models.TextField(max_length=500)

def __str__(self):
    return self.name