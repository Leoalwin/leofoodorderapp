from django.shortcuts import render ,redirect, get_object_or_404
from django.http import *
from .models import *
from decimal import Decimal
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login  as auth_login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import authenticate, logout


# Create your views here.
@login_required
def food_order(request):
    return render(request,"foodorder.html")
@login_required
#Restaurant
def restaurant_reg(request):
    return render(request,"restaurant.html")
@login_required
def restaurant_process(request):
    if request.method =="POST":
        restaurant_id=request.POST.get("restaurant_id")
        rname=request.POST.get("name")
        raddress=request.POST.get("address")
        rphone_number=request.POST.get("phone")
        username=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user1=User.objects.create_user(username=username,email=email,password=password,)
        #ORM
        Restaurant.objects.create(user=user1,restaurant_id=restaurant_id,restaurant_name=rname,username=username,restaurant_email=email,restaurant_address=raddress,restaurant_phone_number=rphone_number)
        group1 = Group.objects.get(name="Restaurants")
        user1.groups.add(group1)
        context={"rname":rname,"username":username,"raddress":raddress,"email":email,"rphone_number":rphone_number}
        return render(request,"restaurantprocess.html",context)
@login_required
def restaurant_details(request):
    res=Restaurant.objects.all()
    return render(request,"restaurantdetails.html",{"restaurant":res})

#Menu
@login_required
def menu_reg(request):
    re=Restaurant.objects.all()
    return render(request,"menu.html",{"restaurant":re}) 
@login_required     
def menu_process(request):
    menu_id=request.POST.get("menu_id")
    mitem=request.POST.get("iname")
    mprice=request.POST.get("price")
    restaurant=request.POST.get("restaurant_id")
    foodimage=request.FILES.get("foodimage")
    pr=Decimal(mprice)
    # rest =Restaurant.objects.get(restaurant_id=restaurant)
    # rest = Restaurant.objects.get(id=restaurant)
    restaurant = Restaurant.objects.get(user=request.user)



    MenuItem.objects.create(menu_id=menu_id,item_name=mitem,price=pr,restaurant=restaurant,image=foodimage)
    context={"mitem":mitem,"pr":pr,"restaurant":restaurant,"foodimage":foodimage}
    
    return render(request,"menuprocess.html",context)
@login_required     
def menu_details(request):
    menu=MenuItem.objects.all()
    return render(request,"menudetails.html",{"menu":menu})

#Customer
@login_required
def customer_reg(request):
    return render (request,"customer.html")
@login_required
def customer_process(request):
    if request.method == "POST":
        customer_id=request.POST.get("customer_id")
        customer_name=request.POST.get("name")
        username=request.POST.get('uname')
        email=request.POST.get("email")
        cphone=request.POST.get("phone")
        caddress=request.POST.get("address")
        password=request.POST.get('password')
        user1=User.objects.create_user(username=username,email=email,password=password)
        Customer.objects.create(user=user1,customer_id=customer_id,customer_name=customer_name,username=username,customer_email=email,customer_password=password,customer_phone_number=cphone,customer_address=caddress)
        group = Group.objects.get(name="Customers")
        user1.groups.add(group)
        context={"customer_name":customer_name,"username":username,"email":email,"cpassword":password,"caddress":caddress,"cphone":cphone} 
        return render(request,"customerprocess.html",context)
@login_required
def customer_details(request):
    cust=Customer.objects.all()
    return render (request,"customeralldetails.html",{"cust":cust})

#Delivery
@login_required
def driver_reg(request):
    return render(request,"driver.html")    
@login_required
def driver_process(request):
    if request.method == "POST":
      driver_id=request.POST.get("driver_id")
      dname=request.POST.get("name")
      dphone=request.POST.get("phone")
      email=request.POST.get("email")
      dlocation=request.POST.get("location")
      username=request.POST.get('uname')
      password=request.POST.get('password')
      user3=User.objects.create_user(username=username,email=email,password=password)
      Driver.objects.create(user=user3,driver_id=driver_id,driver_name=dname,username=username,driver_email=email,driver_phone_number=dphone,driver_current_location=dlocation)
      group = Group.objects.get(name="Delivery")
      user3.groups.add(group)
      context={"dname":dname,"username":username,"email":email,"dphone":dphone,"dlocation":dlocation}
      return render(request,"driverprocess.html",context)
@login_required
def driver_details(request):
    dri=Driver.objects.all()
    return render(request,"driverdetails.html",{"driver":dri})
@login_required     
def rating_reg(request):
    rest=Restaurant.objects.all()
    use=Customer.objects.all()
    return render(request,"rating.html",{"users":use,"restaurants":rest})
def rating_process(request):
    rating_id=request.POST.get("rating_id")
    user=request.POST.get("user")
    restaurant=request.POST("restaurant")
    rating=request.POST("stars")  
    use =Customer.objects.get(user_id=user)
    res =Restaurant.objects.get(restaurant_id=restaurant)
    Rating.objects.create(rating_id=rating_id,user=use,restaurant=res,stars=rating)

    return redirect("ratingadd")
@login_required    
def one_menu(request):
        restaurants=Restaurant.objects.all()
        return render(request, "onemenu.html", {"restaurants": restaurants,})
                            
# @login_required        
# def select_process(request):
#       if request.method == "GET":
#        restaurant_id=request.GET.get("restaurant_id")
#        restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
#        menu=MenuItem.objects.filter(restaurant=restaurant)
#        return render(request, "selectprocess.html", {"menu": menu,"select_restaurant": restaurant,})
#       else:
#          restaurants=Restaurant.objects.all()
#          return render(request,"selectprocess.html",{"restaurant":restaurants})
@login_required
def select_process(request):
    if request.method == "GET":
        restaurant_id = request.GET.get("restaurant_id")
        if restaurant_id:
            restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
            menu = MenuItem.objects.filter(restaurant=restaurant)
            return render(request, "selectprocess.html", {
                "menu": menu,
                "select_restaurant": restaurant,
            })
    # fallback if no restaurant_id is provided
    restaurants = Restaurant.objects.all()
    return render(request, "selectprocess.html", {"restaurant": restaurants})



      
    #   if request.method == "POST":
    #       restaurants=Restaurant.objects.all()
    #       return render(request,"selectprocess.html",{"restaurant":restaurants})
    #   elif request.method == "GET":
    #           restaurant=request.GET.get("restaurant")
    #           restaurant=Restaurant.objects.get(restaurant_id=restaurant)
    #           menu=MenuItem.objects.filter(restaurant_id=restaurant)
    #           restaurants=Restaurant.objects.all()
    #           return render(request, "selectprocess.html", {"menu": menu,"select_restaurant": restaurant,"restaurants":restaurants})



@login_required     
def one_display(request):
   menu_id=request.GET.get("menu_id")
   menu = get_object_or_404(MenuItem, menu_id=menu_id)

   return render(request,"displayone.html",{"Menu":menu})



@login_required     
def order_food(request):
    if request.method == "POST":
        menu_id = request.POST.get("menu_id")
        itemname=request.POST.get("iname")
        restaurant_id=request.POST.get("restaurant")
        mprice=float(request.POST.get("price"))
        quantity = int(request.POST.get("quantity"))
        total_price = quantity * mprice
        request.session['restaurant'] = restaurant_id  
        item = {"menu_id": menu_id,"item_name": itemname,"price": mprice,"quantity": quantity,"total": total_price,}
        cart = request.session.get('cart',[])  
        cart += [item] 
        request.session['cart'] = cart
        restaurant_id = request.session.get('restaurant')

        menu = get_object_or_404(MenuItem, menu_id=menu_id)
        # restaurants=Restaurant.objects.all()
        # restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)


        context ={"menu":{"menu":menu,"restaurants":restaurant_id,"item_name": itemname,"price": mprice,"quantity": quantity, "total": total_price}}
        redirect('selectprocess')
    return render(request, "order.html", context)
@login_required     
def select_food(request):
         if request.method == 'POST':
           rname = request.session.get('restaurant')
           cart = request.session.get('cart')
           print("Cart:", cart)
           return render(request, 'onemenu.html', {"rname": rname, "cart": cart})
         else:
          rname = request.session.get('restaurant')
          return render(request, "order.html", {"rname": rname})
         
@login_required
def select_all(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "clear":
            request.session.clear()
            return render(request, "customerhome.html")

        elif action == "confirm":
            cart = request.session.get('cart', [])
            restaurant_id = request.session.get('restaurant')
            customer = Customer.objects.get(user=request.user)  
            restaurant = Restaurant.objects.get(restaurant_name=restaurant_id)
            print(restaurant_id,customer,restaurant)
            driver = Driver.objects.first() 
            total = sum(float(item['total']) for item in cart)
            order = Order.objects.create(customer=customer,restaurant=restaurant,driver=driver,
                                         total=total,status='pending')
            for item in cart:
                menu_item = MenuItem.objects.get(pk=item['menu_id'])
                order.items.add(menu_item)

            request.session['cart'] = []
            return redirect('payment')  

    else:
        # rname = request.session.get('restaurant')
        cart = request.session.get('cart', [])
        restaurant_name = request.session.get('restaurant')
        restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)
        restaurant_id = restaurant.restaurant_id
        return render(request, 'foodshow.html', {"cart": cart, "rname": restaurant.restaurant_name,"restaurant_id":restaurant.restaurant_id})


def payment_order(request):
    return render(request,"payment.html")  





def login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')
        print("Username ###############", username, "Password", password)
 
        user = authenticate(request,username=username,password=password)
        print("Authenticated user:", user)
        
        if user:
            print(" Hello ! ", user)
           

        if user is not None:
            auth_login(request, user)
            print(" User ", user)
            if user.groups.filter(name='Customers').exists():
              role='Customers'
            elif user.groups.filter(name='Delivery').exists():
              role='Delivery'
            elif user.groups.filter(name='Restaurants').exists():
              role='Restaurants'
            else:
               role='unknown'
            print("Username ", user , " Role : " , role )

            request.session["role"] = role
            request.session["user"] = user.username

            if role == "Restaurants":
                return redirect("restauranthome")
            elif role == "Customers":
                return redirect("customerhome")
            elif role == "Delivery":
                return redirect("deliveryhome") 
        else:
         context = {"error": "Invalid username or password"}
         return render(request, "login.html", context)      
    return render(request, "login.html",)

# @login_required
def view_home(request):
    user = request.user
    role = None
    customer_data = None 

    if user.groups.filter(name='Customers').exists():
        role = 'Customers'
        customer_data = Customer.objects.get(user=user)
    elif user.groups.filter(name='Delivery').exists():
        role = 'Delivery'
    elif user.groups.filter(name='Restaurants').exists():
        role = 'Restaurants'
    else:
        role = 'unknown'
    print( "Username ", user, " Role ", role )
    return render(request, "homepage.html", {"role": role,"user":user})



@login_required
def customer_home(request):
    username = request.session.get("user")
    customer=Customer.objects.get(user__username=username)
    restaurants = None
    show = False
    current_orders = None
    order_history = None
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "Orderfood":
            restaurants = Restaurant.objects.all()
        elif action == "Me":
            show = True
        elif action == "Current Order":
            current_orders = Order.objects.filter(customer=customer, status="Pending")  
        elif action == "Order History":
            order_history = Order.objects.filter(customer=customer).exclude(status="Pending")
        elif action == "Logout":
            logout(request)
            return redirect("login")

        
    context = {"customer": customer,"restaurants": restaurants, "show": show,"current_orders": current_orders,
        "order_history": order_history, } 
    return render(request, "customerhome.html", context)


@login_required
def restaurant_home(request):
    username = request.session.get("user")
    restaurants=Restaurant.objects.get(user__username=username)
    menu = None
    show = False
    orders = None
    drivers = Driver.objects.all()
    selected_order = None
    current_datetime = timezone.now()   
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "Menu Details" :
            menu = MenuItem.objects.filter(restaurant=restaurants)
        elif action == "Restaurant Details":
            show=True
        elif action =="Add Menus":
            return redirect("menu")
        elif action == "View Orders":
            orders = Order.objects.filter(restaurant=restaurants).select_related('customer')
        elif action == "Select":
            order_id = request.POST.get("order_id")
            if action == "select" and order_id:
                selected_order = get_object_or_404(Order, pk=order_id)

            orders = Order.objects.filter(restaurant=restaurants).select_related('customer', 'driver')
        elif action == "Logout":
            logout(request)
            return redirect("login")
    return render(request, "restauranthome.html", {"menu": menu,"restaurant": restaurants,"show":show,"orders": orders, "drivers": drivers,
        "selected_order": selected_order,"current_datetime": current_datetime })
@login_required
def assign_order(request):
    drivers = Driver.objects.all()
    orders = Order.objects.filter(status="pending")
    order = None  

    if request.method == "POST":
        order_id = request.POST.get("order_id")
        action = request.POST.get("action")
        driver_id = request.POST.get("driver_id")

        if order_id:
            order = get_object_or_404(Order, pk=order_id)

            if action == "Accept" and driver_id:
                driver = get_object_or_404(Driver, pk=driver_id)
                order.driver = driver
                order.status = "assigned"
                order.save()
                return redirect("restauranthome")

            elif action == "Decline":
                order.status = "declined"
                order.save()
                return redirect("restauranthome")

    return render(request, "restaurantassign.html", {"order": order, "drivers": drivers})

@login_required
def delivery_home(request):
     username = request.session.get("user")
     delivery=Driver.objects.get(user__username=username)

     show = False
     assigned_orders = False
     orders = [] 
     if request.method == "POST":
         action = request.POST.get("action")
         if action == "Your Profile":
            show = True
         elif action == "Assigned Orders":
            assigned_orders = True
            orders = Order.objects.filter(driver=delivery, status="assigned")

         elif action == "pickup":
           order_id = request.POST.get("order_id")
           order = Order.objects.filter(order_id=order_id, driver=delivery).first()
           if order:
            if order.status == "assigned":
                order.status = "picked up"
                print(order_id,"order status changed to picked up")
            elif order.status == "picked up":
                order.status = "delivered"
                print(order_id, "status changed to 'delivered")
            else:
                print(order_id,"order is already in",order.status)
            order.save()

         elif action == "Past Order":
             last_order = Order.objects.filter(driver=delivery).order_by("-order_id").first()
             if last_order:
                if last_order.status == "assigned":
                  last_order.status = "picked up"
                  print(last_order.order_id,"changed to picked up")
                  last_order.save()
                elif last_order.status == "picked up":
                    last_order.status = "delivered"
                    last_order.save()
             else:
                 orders = [last_order]
         elif action == "Logout":
            logout(request)
            return redirect("login") 
     context = { "show": show ,"delivery":delivery,"assigned_orders": assigned_orders,"orders":orders,} 
     return render(request, "deliveryhome.html", context)







# @login_required
# def assign_order(request):
#     drivers = Driver.objects.all()
#     order = None  

#     if request.method == "POST":
#         order_id = request.POST.get("order_id")
#         action = request.POST.get("action")
#         driver_id = request.POST.get("driver_id")

#         if order_id:
#             order = get_object_or_404(Order, pk=order_id)

#             if action == "Accept" and driver_id:
#                 driver = get_object_or_404(Driver, pk=driver_id)
#                 order.driver = driver
#                 order.status = "assigned"
#                 order.save()
#                 return redirect("restauranthome")

    #         elif action == "Decline":
    #             order.status = "declined"
    #             order.save()
    #             return redirect("restauranthome")

    # return render(request, "restaurantassign.html", {"order": order, "drivers": drivers})
