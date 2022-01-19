from audioop import reverse
from multiprocessing import context
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login
from .models import selling , shouse,rhouse,reqkharid,reqmostager
from .forms import   renthouse,sellhouse,reqbuy,reqrent,mani,userlogin
from django.contrib.auth.decorators import login_required
import datetime
from itertools import chain
from operator import attrgetter

now = datetime.datetime.now().date()
current_datetime = datetime.datetime.now().hour
# Create your views here.
date_1 = datetime.datetime.strptime(str(now), "%Y-%m-%d")
end_date = date_1 + datetime.timedelta(days=1)
end_date = end_date.date()
def home(request): 
    form = userlogin(request.POST)
    if request.method == 'POST':
        print('suck')
        form = userlogin(request.POST)
        if form.is_valid():
            print('fuck')
            cd = form.cleaned_data
            useri = authenticate(request ,email = cd['email'],phone=cd['phone'],password = cd['password'])
            print('fuck you ')
            if useri is not None:
                print('nock nock')
                login(request,useri)
                return redirect('bayatamlak:myfiles')
        
    else :
        form = userlogin()
    return render(request,'login.html',{'form':form})
    # context = {
    #     'selling':selling.objects.all(),
    #     'rent':rent(),
    #     'mog':mog(),
    #     'mos':mos(),
    #     'senti':senti()
    # }    
    # form = mani()
    # if request.method == 'POST':
    #     form = mani(request.POST)
    #     if form.is_valid():
    #         res = form.save(commit=False)
    #         res.moshaver = request.user
    #         res.save()        
    #         return render(request,'reqbuy.html',{'reqbuy':mani})
            
    # return render(request,'home.html',{'reqbuy':mani}) 
# def loglog(request):
    # form = userlogin(request.POST)
    # if request.method == 'POST':
    #     print('suck')
    #     form = userlogin(request.POST)
    #     if form.is_valid():
    #         print('fuck')
    #         cd = form.cleaned_data
    #         useri = authenticate(request ,email = cd['email'],phone=cd['phone'],password = cd['password'])
    #         print('fuck you ')
    #         if useri is not None:
    #             print('nock nock')
    #             login(request,useri)
    #             return redirect('bayatamlak:reqbuy')
        
    # else :
    #     form = userlogin()
        
    # return render(request,'login.html',{'form':form})
def post(request):
    context = {
        'selling':selling.objects.all()
    }
    return render(request,'index.html',context)
@login_required(login_url='/bayatamlak/')
def SubmitRent(request):
    form = renthouse()
    if request.method == 'POST':
        form = renthouse(request.POST)
        if form.is_valid():            
            res = form.save(commit=False)
            res.moshaver = request.user
            res.save()
            return redirect('bayatamlak:myfiles')
    return render(request,'submit_rent.html',{'form':form})
@login_required(login_url='/bayatamlak/')
def Reqbuy(request):
    form = reqbuy()
    if request.method == 'POST':
        form = reqbuy(request.POST, request.FILES )
        if form.is_valid():
            res = form.save(commit=False)
            res.moshaver = request.user
            res.save()
            return redirect('bayatamlak:myfiles')
    return render(request,'reqbuy.html',{'reqbuy':reqbuy})
@login_required(login_url='/bayatamlak/')
def Reqrent(request):
    form = reqrent()
    if request.method == 'POST':
        form = reqrent(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.moshaver = request.user
            res.save()
            return redirect('bayatamlak:myfiles')
            
            
        
    return render(request,'reqrent.html',{'reqrent':reqrent})

@login_required(login_url='/bayatamlak/')    
def SubmitSell(request):
    form = sellhouse()
    if request.method == 'POST':
        form = sellhouse(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.moshaver = request.user
            res.save()
            return redirect('bayatamlak:myfiles')
    return render(request,'submit_sell.html',{'sellhouse':sellhouse})
def about(request):
    context = {
        'selling':selling.objects.all()
    }
    return render(request,'about.html',context)
def contact(request):
    form = reqbuy()
    if request.method == 'POST':
        form = reqbuy(request.POST, request.FILES )
        if form.is_valid():
            res = form.save(commit=False)
            res.moshaver = request.user
            res.save()
    return render(request,'contact.html',{'reqbuy':reqbuy})
def blog(request):
    form = mani()
    if request.method == 'POST':
        form = mani(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.moshaver = request.user
            res.save()
    return render(request,'property_single.html',{'form':mani})

@login_required(login_url='/bayatamlak/')    
def myfile(request):
    sellhouses = shouse.objects.filter(moshaver=request.user)
    renthouses = rhouse.objects.filter(moshaver=request.user)
    reqrental = reqmostager.objects.filter(moshaver=request.user)
    reqbuuy = reqkharid.objects.filter(moshaver=request.user)
    result_list = sorted(list(chain(sellhouses,renthouses,reqrental,reqbuuy)),key=attrgetter('data_created'),reverse=True)
    context = {'result_list':result_list
    }
    return render(request,'myfiles.html',context)
@login_required(login_url='/bayatamlak/')
def reqrents(request):
    context = {'result_list':reqmostager.objects.all().order_by('-data_created')}
    return render(request,'reqrents.html',context)
@login_required(login_url='/bayatamlak/')
def reqbuys(request):
    context = {'result_list':reqkharid.objects.all().order_by('-data_created')}
    return render(request,'reqbuys.html',context)
@login_required(login_url='/bayatamlak/')
def submitrents(request):
    context = {'result_list':rhouse.objects.all().order_by('-data_created')}
    return render(request,'submit_rents.html',context)
@login_required(login_url='/bayatamlak/')
def submitsells(request):
    context = {'result_list':shouse.objects.all().order_by('-data_created')}
    return render(request,'submit_sells.html',context)

@login_required(login_url='/bayatamlak/')    
def sell_detail(request,id):
    sellhouse = shouse.objects.get(id=id)
    
    context = {'form':sellhouse
    }
    return render(request,'sell_detail.html',context)
@login_required(login_url='/bayatamlak/')    
def rent_detail(request,id):
    renthouses = rhouse.objects.get(id=id)
    context = {'form':renthouses
    }
    return render(request,'rent_detail.html',context)

@login_required(login_url='/bayatamlak/')    
def req_buy_detail(request,id):
    reqbuuy = reqkharid.objects.get(id=id)
    context = {'form':reqbuuy
    }
    return render(request,'req_sell_detail.html',context)

@login_required(login_url='/bayatamlak/')    
def req_rent_detail(request,id):
    reqrental = reqmostager.objects.get(id=id)
    context = {'form':reqrental
    }
    return render(request,'req_rent_detail.html',context)