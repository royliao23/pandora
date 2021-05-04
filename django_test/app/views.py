from rest_framework import viewsets,filters
from .models import *
from django.http import HttpResponse,JsonResponse

from django.urls import reverse

from django.http import HttpResponse
from http.client import responses

#from .forms import purchaseFormcreate,jobbyFormcreate()
#from .serializers import EmployeesSerializer
from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date
from django.utils.timezone import get_current_timezone
from django.db.models import F
from django.db.models import Value
from django.db.models import Sum,Q,Count
from django.db.models.functions import Concat
from django.core.paginator import Paginator #import Paginator
from django.db.models import Case, When, Max, FloatField
from django.db.models.functions import ExtractMonth,ExtractYear,Cast, Coalesce
import csv,json
from datetime import *


def showmenu(request):
    messages = Employees.objects.all()
    context = {
           'all_musicians':messages,
    }

    
    return render(request, 'app/main.html', context)
def importdata(request):
        with open('/usr/src/django_test/people1.json') as f:        
            key=0
            data = json.load(f)
            #print(data)
            for x in data:
                
                friendno=[]
                newjb=People()
                newjb._id=x['_id']
                newjb.index=x['index']
                newjb.guid=x['index']
                newjb.has_died=x['has_died']
                y=float(x['balance'][1:].replace(',',''))
                newjb.balance=y  
                
                newjb.picture=x['picture']
                newjb.age=x['age']
                newjb.eyecolor=x['eyeColor']
                newjb.name=x['name']
                newjb.gender=x['gender']
                newjb.company_id=x['company_id']
                newjb.email=x['email'] 
                newjb.phone=x['phone']
                newjb.address=x['address']  
                newjb.about=x['about']
                newjb.registered=datetime.strptime(x['registered'], '%Y-%m-%dT%H:%M:%S %z')
                newjb.tags=x['tags']
                newjb.friends=key
                newjb.greeting=['greeting']
                newjb.favoritefoods=x['favouriteFood']
                newjb.save()

                for fd in x['friends']:         
                    friendno.append(fd['index'])
                
                social=Friend_List()
                social.key=key
                social.friends=friendno
                social.save()
                key=key+1
            return HttpResponse(data)
def importdata2(request):
        with open('/usr/src/django_test/people2.json') as f:        
            key=0
            data = json.load(f)
            #print(data)
            for x in data:
                
                friendno=[]
                newjb=People()
                newjb._id=x['_id']
                newjb.index=x['index']
                newjb.guid=x['index']
                newjb.has_died=x['has_died']
                y=float(x['balance'][1:].replace(',',''))
                newjb.balance=y  
                
                newjb.picture=x['picture']
                newjb.age=x['age']
                newjb.eyecolor=x['eyeColor']
                newjb.name=x['name']
                newjb.gender=x['gender']
                newjb.company_id=x['company_id']
                newjb.email=x['email'] 
                newjb.phone=x['phone']
                newjb.address=x['address']  
                newjb.about=x['about']
                newjb.registered=datetime.strptime(x['registered'], '%Y-%m-%dT%H:%M:%S %z')
                newjb.tags=x['tags']
                newjb.friends=key
                newjb.greeting=['greeting']
                newjb.favoritefoods=x['favouriteFood']
                newjb.save()

                for fd in x['friends']:         
                    friendno.append(fd['index'])
                
                social=Friend_List()
                social.key=key
                social.friends=friendno
                social.save()
                key=key+1
        return HttpResponse(data)
def importcompany(request):
        with open('/usr/src/django_test/companies.json') as f:
            data = json.load(f)
            
            for x in data:
                newjb=Company_Staff()
                peinstance=People.objects.get(index=x['index'])
                newjb.index=peinstance
                newjb.company=x['company']        
                newjb.save()       
        return HttpResponse(data)

def showfriends(request):
    fr=Friend_List.objects.all()
    context={"all":fr}
    return render(request, 'app/fr.html', context)
def showcompany(request):
    fr=Company_Staff.objects.all()
    context={"all":fr}
    return render(request, 'app/companylist.html', context)
def showfood(request):
    fr=People.objects.all()
    context={"all":fr}
    return render(request, 'app/foodlist.html', context)

def apishowfood(request,pk):
    listoffoods=[]
    result = []
    veg=['cucumber','carrot','beetroot', 'celery']
    print(type(veg))
    fruits=['orange','strawberry','banana','apple']
    myveg=[]
    myfruits=[]
    final={}
    

    all=People.objects.all().values('index', 'favoritefoods')
    for rec in all:
        listoffoods.append(rec['favoritefoods'])
    
    
    for sublist in listoffoods:
        mylist = sublist.split(',')
        mylist[0]=mylist[0][1:]
        mylist[-1]=mylist[-1][:-1]
        for item in mylist:
            result.append(item)
    resultunique=list(set(result))
    #print(result)
   
    print(resultunique)


    
    x=People.objects.get(index=pk)
    myfood=x.favoritefoods[1:][:-1]
    myfood=myfood.split(',')
    for f in myfood:
        print(f)
        f=f.replace("'", '').strip()
        print(f)
        
        if f in veg:
            
            myveg.append(f)
        else:
           
            myfruits.append(f)
    
    final['name']=x.name
    final['age']=x.age
    final['fruits']=myfruits
    final['veg']=myveg
    
        
    print(final)


    if final:
        return JsonResponse(final,safe=False)
    else:
        return JsonResponse({'error':'no such a people code!'},safe=False)
    
    #return JsonResponse(fr,safe=False)
    #return HttpResponse(fr, content_type='application/json')
    #return HttpResponse(json.dumps(fr,indent=4, sort_keys=True, default=str))
    
def apishowcompany(request,pk):
    fr=Company_Staff.objects.filter(Q(pk=pk))
    if fr:
        result_list = list(fr.values())
        return JsonResponse(result_list,safe=False)
    else:
        return JsonResponse({'error':'no such a company code!'},safe=False)
def checkaliveandeye(num):
    p=People.objects.get(index=num)
    
    if (p.eyecolor=='brown') & (p.has_died==False):
            return True
    else:
            return  False


def apishowalive(request,pk1,pk2):
    
    person1=[]
    person2=[]
    mutualalivebrown=[]
    # User.objects.filter(first_name__startswith='R').values('first_name', 'last_name')
    fr1=People.objects.filter(Q(pk=pk1)).values('index','name', 'age','address','phone','friends')
    
    fr2=People.objects.filter(Q(pk=pk2)).values('index','name', 'age','address','phone','friends')
    
    for f1 in fr1:
        person1.append(f1['name'])
        person1.append(f1['age'])
        person1.append(f1['address'])
        person1.append(f1['phone'])

        f1no=f1['friends']
        f1list=Friend_List.objects.filter(Q(key=f1no))
        for x in f1list:
            list1=x.friends
            
        mylist = list1.split(',')
        mylist[0]=mylist[0][1:]
        mylist[-1]=mylist[-1][:-1]
        list1=[int(i) for i in mylist ]
        
    for f2 in fr2:
        person2.append(f1['name'])
        person2.append(f1['age'])
        person2.append(f1['address'])
        person2.append(f1['phone'])
        f2no=f2['friends']
        f2list=Friend_List.objects.filter(Q(key=f2no))
        for y in f2list:
            list2=y.friends
        mylist = list2.split(',')
        mylist[0]=mylist[0][1:]
        mylist[-1]=mylist[-1][:-1]
        list2=[int(i) for i in mylist ]
     
    
    mutual_list=[x for x in list1 if x in list2]
    mutual_list=[ int(i) for i in mutual_list ]
    
    for a in mutual_list:
        if checkaliveandeye(a):
            mutualalivebrown.append(a)
    final_list={}
    final_list['p1']=person1
    final_list['p2']=person2
    final_list['mfriend']=mutual_list
    final_list['mutualalivebrowneye']=mutualalivebrown
    
    return JsonResponse(final_list,safe=False)
   

def localimportdata(request):
        with open('C:\code\django_project\django_test\people.json') as f:        
            key=0
            data = json.load(f)
            #print(data)
            for x in data:
                
                friendno=[]
                print(x['_id'])
                print("=================================")
                print(x['guid'])
                print("=================================")
                print(x['friends'])
                newjb=People()
                newjb._id=x['_id']
                newjb.index=x['index']
                newjb.guid=x['index']
                newjb.has_died=x['has_died']
                y=float(x['balance'][1:].replace(',',''))
                newjb.balance=y  
                
                newjb.picture=x['picture']
                newjb.age=x['age']
                newjb.eyecolor=x['eyeColor']
                newjb.name=x['name']
                newjb.gender=x['gender']
                newjb.company_id=x['company_id']
                newjb.email=x['email'] 
                newjb.phone=x['phone']
                newjb.address=x['address']  
                newjb.about=x['about']
                newjb.registered=datetime.strptime(x['registered'], '%Y-%m-%dT%H:%M:%S %z')
                newjb.tags=x['tags']
                newjb.friends=key
                newjb.greeting=['greeting']
                newjb.favoritefoods=x['favouriteFood']
                newjb.save()

                for fd in x['friends']:         
                    friendno.append(fd['index'])
                
                social=Friend_List()
                social.key=key
                social.friends=friendno
                social.save()
                key=key+1
            return HttpResponse(data)
    

def localimportcompany(request):
        with open('C:\code\django_project\django_test\companies.json') as f:
            data = json.load(f)
            
            for x in data:
                print(x['index'])
                print("=================================")
                print(x['company'])
                print("=================================")  
                newjb=Company_Staff()
                peinstance=People.objects.get(index=x['index'])
                newjb.index=peinstance
                newjb.company=x['company']     
                newjb.save()
                      
            return HttpResponse(data)
    

