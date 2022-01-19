from collections import defaultdict
from django.db import models
from django.db.models.enums import Choices
from django.db.models.expressions import Value
from django.db.models.fields import CharField
# from django_jalali.db import models as jmodels
# from phonenumber_field.modelfields import PhoneNumberField
# from multiselectfield import MultiSelectField
import datetime
from django.core.validators import MinLengthValidator
# from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser
now = str(datetime.datetime.now().date())
now2 = str(datetime.datetime.now().hour)
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class MyUserManager(BaseUserManager):
    def create_user(self,email,phone,password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,phone,password):
        user = self.create_user(
            email,
            password=password,
            phone=phone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    name = models.CharField(max_length=20,verbose_name='نام مشاور',default='مانی')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        return self.is_admin

class HouseAbastract(models.Model):
    title = models.CharField(verbose_name=' نام ملک',max_length=100)
    Name = models.CharField(verbose_name='نام ',max_length=50,default='بزرگ')
    Phone =  models.CharField(verbose_name='تلفن ',max_length=11,default= 91234567891 )
    moshaver = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='مشاور')
    room = models.SmallIntegerField(verbose_name='تعداد اتاق ها')
    elsei2 = models.CharField(max_length=30,verbose_name='پروژه',default='noting')
    class Meta:
        abstract = True

class rhouse(HouseAbastract):
    MY_CHOICES = (('پکیج', 'پکیج '),
              ('کولر', 'کولر'),
              ('کابینت', 'کابینت'),
              ('هود', 'هود'),
              ('رادیاتور', 'رادیاتور'),
              ('کمد دیواری', 'کمد دیواری'),
              ('انباری', 'انباری'),
              ('پارکینگ', 'پارکینگ'),
              ('آسانسور', 'آسانسور'),
              ('گاز رو میزی', 'گاز رو میزی'),
              (' آیفون تصویری', 'آیفون تصویری'),
              ('روشنایی', 'روشنایی'),
              (' درب اکاردونی', 'درب اکاردونی'))
    
    # MojerFamily = models.CharField(verbose_name='نام خانوادگی موجر',max_length=50)
    
    rahn = models.CharField(verbose_name='رهن',max_length=11)
    ejare = models.CharField(verbose_name='اجاره',max_length=11)
    size = models.IntegerField(verbose_name='متراژ')         
    phase = models.SmallIntegerField(verbose_name='فاز')
    Floor = models.SmallIntegerField(verbose_name='طبقه')
    Address = models.TextField(verbose_name='ادرس')
    elsei = models.TextField(verbose_name='توضیحات')
    data_created = models.DateTimeField(verbose_name='تاریخ ایجاد' , auto_now_add=True,null=True,blank=True)
    position = models.CharField(max_length=20 ,verbose_name='ویژگی',default='اجاره',editable=False)
    # facility = MultiSelectField(choices=MY_CHOICES,null=True,verbose_name='امکانات') 
    # image = models.ImageField(null=True, blank=True, verbose_name= 'عکس اصلی ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    # image1 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image2 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image3 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    # image4 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image5 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image6 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image7 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # def __str__(self):
    #     return self.MojerName
    class Meta:
        verbose_name = 'ملک اجاره'
        verbose_name_plural = " ملک های اجاره"


class shouse(HouseAbastract):
    MY_CHOICES = (('پکیج', 'پکیج '),
              ('کولر', 'کولر'),
              ('کابینت', 'کابینت'),
              ('هود', 'هود'),
              ('رادیاتور', 'رادیاتور'),
              ('کمد دیواری', 'کمد دیواری'),
              ('انباری', 'انباری'),
              ('پارکینگ', 'پارکینگ'),
              ('آسانسور', 'آسانسور'),
              ('گاز رو میزی', 'گاز رو میزی'),
              (' آیفون تصویری', 'آیفون تصویری'),
              ('روشنایی', 'روشنایی'),
              (' درب اکاردونی', 'درب اکاردونی'))
    price = models.CharField(verbose_name='قیمت',max_length=11)
    size = models.IntegerField(verbose_name='متراژ')       
    phase = models.SmallIntegerField(verbose_name='فاز')
    Floor = models.SmallIntegerField(verbose_name='طبقه')
    Address = models.TextField(verbose_name='ادرس')
    elsei = models.TextField(verbose_name='توضیحات')
    data_created = models.DateTimeField(verbose_name='تاریخ ایجاد' , auto_now_add=True,null=True,blank=True)
    position = models.CharField(max_length=20 ,verbose_name='ویژگی',default='فروشی',editable=False)
    # facility = MultiSelectField(choices=MY_CHOICES,null=True,verbose_name='امکانات') 
    # image = models.ImageField(null=True, blank=True, verbose_name= 'عکس اصلی ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    # image1 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image2 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image3 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    # image4 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image5 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image6 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # image7 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # def __str__(self):
    #     return self.SellerName
    class Meta:
        verbose_name = 'ملک فروش'
        verbose_name_plural = "ملک های فروشی "


class rental(models.Model):
    moshaver = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='مشاور')
    MojerName = models.CharField(verbose_name='نام موجر',max_length=50,default='علی')
    MojerFamily = models.CharField(verbose_name='نام خانوادگی موجر',max_length=50,default='قاسمی')
    # MojerBirth = jmodels.jDateField(verbose_name='تاریخ تولد موجر',default='1400-10-10')
    MojerMeliCode = models.CharField(max_length=10, verbose_name='کد ملی موجر',default='0123456789')
    MojerPhone =  models.CharField(max_length=11, verbose_name='تلفن موجر',default='09123456789')
    MostajerName = models.CharField(verbose_name='نام مستاجر ',max_length=50,default='علی')
    MostajerFamily = models.CharField(verbose_name='نام خانوادگی مستاجر ',max_length=50,default='قاسمی')
    # MostajerBirth = jmodels.jDateField(verbose_name='تاریخ تولد مستاجر ',default='1400-10-10')
    MostajerMeliCode = models.CharField(max_length=10, verbose_name='کد ملی مستاجر ',default='0123456789')
    MostajerPhone =  models.CharField(max_length=11, verbose_name='تلفن مستاجر ',default='09123456789')
    Paravande = models.CharField(max_length=7,verbose_name='شماره قرارداد',unique=True,default='10')
    MY_CHOICES = (('پکیج', 'پکیج '),
              ('کولر', 'کولر'),
              ('کابینت', 'کابینت'),
              ('هود', 'هود'),
              ('رادیاتور', 'رادیاتور'),
              ('کمد دیواری', 'کمد دیواری'),
              ('انباری', 'انباری'),
              ('پارکینگ', 'پارکینگ'),
              ('آسانسور', 'آسانسور'),
              ('گاز رو میزی', 'گاز رو میزی'),
              (' آیفون تصویری', 'آیفون تصویری'),
              ('روشنایی', 'روشنایی'),
              (' درب اکاردونی', 'درب اکاردونی'))

    price = models.BigIntegerField(verbose_name='قیمت')
    size = models.IntegerField(verbose_name='متراژ')       
    room = models.SmallIntegerField(verbose_name='تعداد اتاق ها')  
    phase = models.SmallIntegerField(verbose_name='فاز')
    Floor = models.SmallIntegerField(verbose_name='طبقه')
    Address = models.TextField(verbose_name='ادرس')
    elsei = models.TextField(verbose_name='توضیحات')
    # facility = MultiSelectField(choices=MY_CHOICES,null=True,verbose_name='امکانات') 
    image = models.ImageField(null=True, blank=True, verbose_name= 'عکس اصلی ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    image1 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image2 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image3 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    image4 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image5 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image6 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image7 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    # def __str__(self):
    #     return self.MojerName
    class Meta:
        verbose_name = 'بایگانی اجاره '
        verbose_name_plural = "بایگانی های اجاره "

class selling(models.Model):
    moshaver = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='مشاور')
    BuyerName = models.CharField(verbose_name='نام خریدار',max_length=50)
    BuyerFamily = models.CharField(verbose_name='نام خانوادگی خریدار',max_length=50)
    # BuyerBirth = jmodels.jDateField(verbose_name=' تاریخ تولدخریدار')
    BuyerMeliCode = models.CharField(max_length=10,verbose_name='کد ملی خریدار' )
    BuyerPhone =  models.CharField(max_length=11,verbose_name='تلفن خریدار')
    SellerName = models.CharField(verbose_name='نام فروشنده',max_length=50)
    SellerFamily = models.CharField(verbose_name='نام خانوادگی  فروشنده',max_length=50)
    # SellerBirth = jmodels.jDateField(verbose_name='تاریخ تولد فروشنده')
    SellerMeliCode = models.CharField(max_length=10,verbose_name='کد ملی فروشنده')
    SellerPhone =  models.CharField(max_length=11,verbose_name='تلفن  فروشنده')
    MY_CHOICES = (('پکیج', 'پکیج '),
              ('کولر', 'کولر'),
              ('کابینت', 'کابینت'),
              ('هود', 'هود'),
              ('رادیاتور', 'رادیاتور'),
              ('کمد دیواری', 'کمد دیواری'),
              ('انباری', 'انباری'),
              ('پارکینگ', 'پارکینگ'),
              ('آسانسور', 'آسانسور'),
              ('گاز رو میزی', 'گاز رو میزی'),
              (' آیفون تصویری', 'آیفون تصویری'),
              ('روشنایی', 'روشنایی'),
              (' درب اکاردونی', 'درب اکاردونی'))
    price = models.BigIntegerField(verbose_name='قیمت')
    size = models.IntegerField(verbose_name='متراژ')       
    phase = models.SmallIntegerField(verbose_name='فاز')
    Floor = models.SmallIntegerField(verbose_name='طبقه')
    Address = models.TextField(verbose_name='ادرس')
    elsei = models.TextField(verbose_name='توضیحات')
    # facility = MultiSelectField(choices=MY_CHOICES,null=True,verbose_name='امکانات') 
    image = models.ImageField(null=True,blank=True, verbose_name= 'عکس اصلی ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    image1 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image2 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image3 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to = f'home/{now}/{now2}/', default='default.jpg')
    image4 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image5 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image6 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    image7 = models.ImageField(null=True,blank=True, verbose_name= 'عکس ', upload_to =  f'home/{now}/{now2}/', default='default.jpg')
    class Meta:
        verbose_name = ' بایگانی فروش'
        verbose_name_plural = " بایگانی های فروش "
    
class reqmostager(HouseAbastract):
    MY_CHOICE = (
        ('شخصی ساز','شخصی ساز'),
        ('مسکن مهر','مسکن مهر'),
        ('ویلایی ','ویلایی '),
        ('اداری ','اداری '),
        ('تجاری','تجاری')
        )
    rahn = models.IntegerField(verbose_name='رهن')
    ejare = models.IntegerField(verbose_name='اجاره')
    phase = models.IntegerField(verbose_name='فاز')
    elsei = models.TextField(verbose_name='توضیحات')
    # elesi1 = models.CharField(max_length=20,choices=MY_CHOICE,verbose_name='انتخابی ',default='تجاری')
    
    data_created = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True,null=True,blank=True)
    position = models.CharField(max_length=20 ,verbose_name='ویژگی',default='درخواست اجاره',editable=False)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درخواست اجاره'
        verbose_name_plural = "درخواست های اجاره"


class reqkharid(HouseAbastract):
    MY_CHOICE = (
        ('شخصی ساز','شخصی ساز'),
        ('مسکن مهر','مسکن مهر'),
        ('ویلایی ','ویلایی '),
        ('اداری ','اداری '),
        ('تجاری','تجاری'),
        ('زمین','زمین')
        )
    
    mojodi = models.IntegerField(verbose_name='موجودی')
    phase = models.IntegerField(verbose_name='فاز')
    elsei = models.TextField(verbose_name='توضیحات')
    # elesi1 = models.CharField(max_length=20,choices=MY_CHOICE,verbose_name='انتخابی ')
    data_created = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True,null=True,blank=True)
    position = models.CharField(max_length=20 ,verbose_name='ویژگی',default='درخواست خرید',editable=False)
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'درخواست خرید'
        verbose_name_plural = "درخواست های خرید"

class mani(models.Model):
    moshaver = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='مشاور',null=True,blank=True)
    datei = models.DateField()
    mani = models.IntegerField()

