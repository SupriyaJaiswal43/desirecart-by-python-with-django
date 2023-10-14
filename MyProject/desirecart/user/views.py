from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from . models import *
from django.db import connection
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    mproduct=product.objects.all().order_by('-id')[0:8]
    noofitemsincart=""
    if request.user.is_authenticated:
        uname=request.user
        noofitemsincart=addtocart.objects.filter(userid=uname,status=True).count()

    return render(request, 'user/index.html', {"mixproduct": mproduct,"cart":noofitemsincart})

#############################3##

def mensproduct(request):
    noofitemsincart = ""
    a=request.GET.get('msg')
    if a==None:
        pdata=product.objects.filter(category='Mens')
    else:
        pdata=product.objects.filter(category='Mens',subcategory=a)
    scat=subcategory.objects.all().order_by('-id')
    if request.user.is_authenticated:
        uname=request.user
        noofitemsincart=addtocart.objects.filter(userid=uname,status=True).count()
    return  render(request,'user/mensproduct.html',{"data":pdata,"subcat":scat,"cart":noofitemsincart})

################################

def wproduct(request):
    noofitemsincart = ""
    a = request.GET.get('msg')
    if a == None:
        pdata = product.objects.filter(category='Womens')
    else:
        pdata = product.objects.filter(category='Womens', subcategory=a)
    scat = subcategory.objects.all().order_by('-id')
    if request.user.is_authenticated:
        uname=request.user
        noofitemsincart=addtocart.objects.filter(userid=uname,status=True).count()
    return render(request, 'user/wproduct.html',{"data":pdata,"subcat":scat,"cart":noofitemsincart})

#################################################

def kproduct(request):
    noofitemsincart=""
    a = request.GET.get('msg')
    if a == None:
        pdata = product.objects.filter(category='Kids')
    else:
        pdata = product.objects.filter(category='Kids', subcategory=a)
    scat = subcategory.objects.all().order_by('-id')
    if request.user.is_authenticated:
        uname = request.user
        noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()
    return render(request, 'user/kproduct.html',{"data":pdata,"subcat":scat,"cart":noofitemsincart})

################################

def contactus(request):
    noofitemsincart=""
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Email=request.POST.get("email","")
        Mobile = request.POST.get("mobno","")
        Message=request.POST.get("msg","")
        res=contactinfo(name=Name,email=Email,mobno=Mobile,msg=Message)
        res.save()
        status=True
    if request.user.is_authenticated:
        uname = request.user
        noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()
    return render(request,'user/contact.html',context={"msgs":status,"cart":noofitemsincart})

def feedback(request):
    pdata = feedbackinfo.objects.all()
    noofitemsincart=""
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Pic = request.FILES.get("img", "")
        State = request.POST.get("state", "")
        Message = request.POST.get("msg", "")
        res = feedbackinfo(name=Name, img=Pic, state=State, msg=Message)
        res.save()
    if request.user.is_authenticated:
        uname = request.user
        noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()
    return render(request, 'user/feedback.html',{"data1": pdata,"cart":noofitemsincart})


#################################################

def myorders(request):
    deliveredProduct=""
    uname=request.user
    orderdetails=""
    noofitemsincart = ""
    deliveredProduct=""
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute("select o.pid,o.userid,o.remarks,o.status,o.odate,p.name,p.disprice,p.size,p.color,p.description,p.ppic,p.id from user_order o, user_product p where o.pid=p.id and o.userid='"+str(uname)+"' and o.status=True and o.remarks='pending for admin' order by o.id desc")
        orderdetails = cursor.fetchall()
        cursor.execute("select o.pid,o.userid,o.remarks,o.status,o.odate,p.name,p.disprice,p.size,p.color,p.description,p.ppic from user_order o, user_product p where o.pid=p.id and o.userid='"+str(uname)+"' and o.status=True and o.remarks='Delivered' order by o.id desc")
        deliveredProduct=cursor.fetchall()
        uname = request.user
        noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()
        cid = request.GET.get('del')
        if request.GET.get('del'):
            a = order.objects.filter(pid=cid)
            a.delete()
            return HttpResponse("<script>alert('Order cancel successfully...');window.location.href='/user/orders/';</script>")
    return  render(request,'user/myorders.html',{"order":orderdetails,"dorder":deliveredProduct,"cart":noofitemsincart})




#################################################

def myprofile(request):
    noofitemsincart =""
    userdetails="";
    if request.user.is_authenticated:
        uname = request.user
        data = signup.objects.filter(email=uname)
        if request.user.is_authenticated:
            uname = request.user
            noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()
            userdetails=signup.objects.filter(email=uname)
            if request.method=="POST":
                name=request.POST['name']
                mobile=request.POST['mobile']
                upic=request.FILES['fu']
                address=request.POST['address']
                res=signup(email=uname,name=name,mobile=mobile,address=address,userpic=upic)
                res.save()




        return  render(request,'user/myprofile.html',{"mdata":data,"cart":noofitemsincart,"udetails":userdetails})
    return HttpResponse("<script>alert('Please login first');window.location.href='/user/signin/';</script>")

#################################################

def viewproduct(request):
    noofitemsincart =""
    pid=request.GET.get('pid')
    data=product.objects.filter(id=pid)

    if request.user.is_authenticated:
        uname = request.user
        noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()
    return  render(request,'user/viewproduct.html',{"pdata":data,"cart":noofitemsincart})


#################################################

def register(request):
    noofitemsincart =""
    status = False
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Mobile = request.POST.get("mobile", "")
        Email = request.POST.get("email", "")
        Password = request.POST.get("password", "")
        CPassword = request.POST.get("cpassword", "")
        Pic = request.FILES.get("userpic", "")
        Address = request.POST.get("address", "")
        res = signup(name=Name,mobile=Mobile, email=Email,  password=Password,cpassword=CPassword,userpic=Pic,address=Address)
        res.save()
        myuser=User.objects.create_user(Email,Email,Password)
        myuser.first_name=Name
        myuser.last_name=Name
        myuser.save()
        status = True
    if request.user.is_authenticated:
        uname = request.user
        noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()
    return render(request, 'user/register.html', context={"msgs": status,"cart":noofitemsincart})


#########################################

def signin(request):
    if request.user.is_authenticated:
        page=request.GET.get('page')
        pid=request.GET.get('pid')
        username=request.user
        if page=='cart':
            checkItem=addtocart.objects.filter(pid=pid,userid=username,status=True)
            if checkItem:
                return render(request, 'user/signin.html', context={"alreadyadded": True})

            savetocart = addtocart(pid=pid, userid=username, status=True, odate=datetime.now().date())
            savetocart.save()
        elif page=='order':
            savetoorder=order(pid=pid,userid=username,remarks="pending for admin",status=True,odate=datetime.now().date())
            savetoorder.save()
            return HttpResponse("<script>alert('Your order is confirmed..');window.location.href='/user/orders/';</script>")

        elif page=='orderfromcart':
            cartrecord=addtocart.objects.filter(pid=pid,userid=username,status=True)
            cartrecord.delete()
            savetoorder = order(pid=pid, userid=username, remarks="pending for admin", status=True,odate=datetime.now().date())
            savetoorder.save()
            return HttpResponse("<script>alert('Your order is conformed');window.location.href='/user/orders/';</script>")

        return render(request, 'user/signin.html', context={"alreadylogin": True})
    else:
        print("Not ok")
        return render(request,'user/signin.html')

#################### Code to Login ##########################

def signin1(request):
    if request.method == 'POST':
        username = request.POST.get("uname", "")
        password = request.POST.get("password", "")
        user=auth.authenticate(username=username,password=password)
        #print user
        if user is not None:
            login(request,user)
            return render(request, 'user/signin.html', context={"User": True})
        else:
            return render(request, 'user/signin.html', context={"Nouser": True})


def logout1(request):
    logout(request)
    return render(request,'user/index.html')


def cartItems(request):
    noofitemsincart =""
    cartvalue=""
    uname=request.user
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute("select p.id,p.name,p.price,p.disprice,p.size,p.color,p.ppic,c.userid,c.odate,c.id,c.status from user_product p, user_addtocart c where p.id=c.pid and userid='"+str(uname)+"' and status=True")
        cartvalue=cursor.fetchall()
        cid=request.GET.get('del')
        if request.GET.get('del'):
            a=addtocart.objects.filter(id=cid)
            a.delete()
            return HttpResponse("<script>alert('Item removed from cart successfully...');window.location.href='/user/cart/';</script>")

    if request.user.is_authenticated:
        uname = request.user
        noofitemsincart = addtocart.objects.filter(userid=uname, status=True).count()

    return render(request,'user/cart.html',{"cartItems":cartvalue,"cart":noofitemsincart})