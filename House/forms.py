from re import L
from django.db import models
from django.forms import widgets
from django.forms.widgets import RadioSelect
from .models import  rental,selling ,reqmostager,reqkharid, rhouse,shouse,mani,User
from django.forms import ModelForm , Textarea
from django import forms

class rent(ModelForm):
    
    class Meta:
        model = rental
        exclude =['moshaver']
class mani(ModelForm):
    
    class Meta:
        model = mani
        exclude =['moshaver']
        labels ={ 'datei':'datei','mani':'mani'}

class sell(ModelForm):
    
    class Meta:
        model = selling
        exclude =['moshaver']
        labels ={'title':'title','SellerName':'SellerName','SellerFamily':'SellerFamily',
                'SellerPhone':'SellerPhone','moshaver':'moshaver','price':'price',
                'size':'size','room':'room','phase':'phase','Floor':'Floor','Address':'Address',
                    'elsei':'elsei','facility':'facility'}

class reqrent(ModelForm):
    
    class Meta:
        model = reqmostager
        exclude =['moshaver']
        labels ={'title':'title','Name':'Name','Phone':'Phone',
                'rahn':'rahn','ejare':'ejare','phase':'phase',
                'elsei2':'elsei2','room':'room','elsei':'elsei',}

class reqbuy(ModelForm):
    
    class Meta:
        model = reqkharid
        exclude =['moshaver']
        labels ={'title':'title','Name':'Name','Phone':'Phone',
                'mojodi':'mojodi','elsei':'elsei',
                'room':'room','phase':'phase','elsei2':'elsei2'}
        

class renthouse(ModelForm):
    class Meta:
        model = rhouse
        exclude =['moshaver']
        labels ={'title':'title','Name':'Name',
                'Phone':'Phone','rahn':'rahn','ejare':'ejare',
                'size':'size','room':'room','phase':'phase','Floor':'Floor','Address':'Address',
                    'elsei':'elsei','elsei2':'elsei2'}

class sellhouse (ModelForm):
    
    class Meta:
        model = shouse
        exclude =['moshaver']
        labels ={'title':'title','Name':'Name',
                'Phone':'Phone','price':'price',
                'size':'size','room':'room','phase':'phase','Floor':'Floor','Address':'Address',
                    'elsei':'elsei','elsei2':'elsei2'}

class userlogin (forms.Form):
    email = forms.EmailField(label='email')
    phone = forms.CharField(label='phone')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    