from django.urls import path
from .views import home,login,SubmitRent,SubmitSell,about,contact,blog,Reqbuy,Reqrent,myfile,reqrents,reqbuys,submitrents,submitsells,sell_detail,rent_detail,req_rent_detail,req_buy_detail
from django.contrib.auth import views as auth_views

app_name = 'bayatamlak'
urlpatterns = [
    path('',home,name = 'home'),
    path('login/',login,name='login'),
    path('submitsell/',SubmitSell,name='submitsell'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),
    path('reqrent/',Reqrent,name='reqrent'),
    path('reqbuy/',Reqbuy,name='reqbuy'),
    path('submitrent/',SubmitRent,name='submitrent'),
    path('reqrents/',reqrents,name='reqrents'),
    path('reqbuys/',reqbuys,name='reqbuys'),
    path('submitrents/',submitrents,name='submitrents'),
    path('submitsells/',submitsells,name='submitsells'),
    # path('myfile/',myfile,name='myfile')
    path('myfiles/',myfile,name='myfiles'),
    path('sell_detail/<int:id>/',sell_detail,name='sell_detail'),
    path('rent_detail/<int:id>/',rent_detail,name='rent_detail'),
    path('req_rent_detail/<int:id>/',req_rent_detail,name='req_rent_detail'),
    path('req_buy_detail/<int:id>/',req_buy_detail,name='req_buy_detail')
]