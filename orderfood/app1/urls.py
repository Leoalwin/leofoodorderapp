from django.urls import path
from .import views

urlpatterns=[
        path("foodorder",views.food_order,name="foodorder"),
        path("restaurant",views.restaurant_reg,name="restaurant"),
        path("resprocess",views.restaurant_process,name="resprocess"),
        path("menu",views.menu_reg,name="menu"),
        path("menuprocess",views.menu_process,name="menuprocess"),
        path("user",views.customer_reg,name="user"),
        path("userprocess",views.customer_process,name="userprocess"),
        path("rating",views.rating_reg,name="rating"),
        path("ratingadd",views.rating_process,name="ratingadd"),
        path("driver",views.driver_reg,name="driver"),
        path("driverprocess",views.driver_process,name="driverprocess"),
        path("userdetail",views.customer_details,name="userdetail"),
        path("restaurantdetail",views.restaurant_details,name="restaurantdetail"),
        path("driverdetail",views.driver_details,name="driverdetail"),
        path("menudetail",views.menu_details,name="menudetail"),
        path("onemenu",views.one_menu,name="onemenu"),
        path("onedisplay",views.one_display,name="onedisplay"),
        path("orderfood",views.order_food,name="orderfood"),
        path("selectprocess",views.select_process,name="selectprocess"),
        path("selectfood",views.select_food,name="selectfood"),
        path("totalfood",views.select_all,name="totalfood"),
        path("payment",views.payment_order,name="payment"), 
        path("login",views.login,name="login"),
        path("home",views.view_home,name="home"),
        path("customerhome",views.customer_home,name="customerhome"),
        path("restauranthome",views.restaurant_home,name="restauranthome"),
        path("deliveryhome",views.delivery_home,name="deliveryhome"),
        path('assign_order', views.assign_order, name='assign_order'),




]