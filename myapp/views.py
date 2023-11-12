from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import datetime
import news
from .models import article
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User , Group , Permission
from manager.models import Manager
import random
import string
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from bs4 import BeautifulSoup
from urllib import request as rq






def index(request):
   
    article_var=  article.objects.get(pk=5)
    
    news=  News.objects.filter(act=1).order_by('-pk')
    
    cat= Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews=  News.objects.filter(act=1).order_by('-pk')[:3]
    
    
    popularnews=  News.objects.filter(act=1).order_by('-show')
    popularnews2=  News.objects.filter(act=1).order_by('-show')[:3]
    
    trending= Trending.objects.all().order_by('-pk')
    
    lastnews2 =  News.objects.filter(act=1).order_by('-pk')[:4]
    
    return render(request, 'front/index.html',{'name':article_var, 'News': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews, 'popularnews': popularnews, 'popularnews2':popularnews2, 'trending':trending, 'lastnews2':lastnews2 })

def about(request):
    article_var= article.objects.get(pk=5)
    
    news=  News.objects.all().order_by('-pk')
    cat= Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews=  News.objects.all().order_by('-pk')[:3]
    
    
    popularnews=  News.objects.all().order_by('-show')
    popularnews2=  News.objects.all().order_by('-show')[:3]
    
    trending= Trending.objects.all().order_by('-pk')[:5]
    
    
    quotes_url = 'https://www.w3schools.com/'
    connect = rq.urlopen(quotes_url)
    page_html = connect.read()
    connect.close()
    parse_page = BeautifulSoup(page_html, 'html.parser')
    heading = parse_page.h1.text.strip()
    print(heading)
    main_quotes = parse_page.find_all('div', {'class': 'servicebox'})
    print(main_quotes)
    
    for service_iter in main_quotes:
        padding = service_iter.find_all('div', {'class': 'w3-padding'})
        service = padding[0].text.strip()
        serviceslinks = service_iter.find_all('a', {'class': 'serviceslink'})
        servicelinks = serviceslinks[0].text.strip()
        print(service, servicelinks)
         

    
    
    return render(request, 'front/about.html',{'name':article_var, 'News': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews, 'popularnews': popularnews, 'popularnews2':popularnews2, 'trending':trending, 'service':service, 'servicelinks': servicelinks})

def admin_panel(request):
    
    #Login check starts Here:
    
    if not request.user.is_authenticated:
        
        return redirect('mylogin')
    #Login Check Ends Here
    
    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms:
        if i.codename == 'master_user': perm = 1
    if perm == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})
    
    
    randnum = random.randint(0, 100000000000)
    print(randnum)
    
    spchar = [':', '@', '#', '$', '&', '(',')']
    randstr = ""
    for i in range(10):
        randstr = randstr+random.choice(string.ascii_letters)
        randstr += random.choice(spchar)
        randstr += str(random.randint(0, 9))
        
        
    count = News.objects.count()
    randnews= News.objects.all()[random.randint(0,count-1)]
    
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if (len(str(day)))==1:
        day = '0' + str(day)
    if (len(str(month)))==1:
        month = '0' + str(month)
    date = str(year)+'-'+str(month)+'-'+str(day)
    
        
            
            
    
        
        

    
    return render(request, 'back/home.html', {'randnum': randnum, 'randstr': randstr, 'randnews': randnews})



    # now = datetime.datetime.now()
    # html= "<h1>Time is now %s.</h1>" % now
    # return HttpResponse(html)
    
    
def mylogin(request):
    
    if request.method == 'POST':
        
       user = request.POST.get('username')
       upass = request.POST.get('password')
       
       if user !="" and upass !="":
           user= authenticate(username=user,password=upass) 
           
           if user != None:
               login(request, user)
               return redirect('panel')
       print(user,upass)
    
    return render(request, 'front/login.html')


def myregister(request):
    
    if request.method == 'POST':
        name= request.POST.get('name')
        uname= request.POST.get('uname')
        email= request.POST.get('email')
        password= request.POST.get('password')
        password1= request.POST.get('password1')
        
        if name == "":
            msg= 'Please Enter your Name'
            return render(request, 'front/message.html', {'msg': msg})
        
        
        if password != password1 :
            msg= 'Password didnt match'
            return render(request, 'front/message.html', {'msg': msg})
        
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in password:
            if i > '0' and i < '9':
                count1 += 1
            if i > 'A' and i < 'Z':
                count2 += 1
            if i > 'a' and i < 'z':
                count3 += 1
            if i > '!' and i < ')':
                count4 += 1
        count = count1 + count2 + count3 + count4
        strength = len(password)
        if count >= 1 and strength < 8:
            msg = 'Weak Password'
            return render(request,'front/message.html', {'msg':msg})

        if len(User.objects.filter(username=uname))== 0 and len(User.objects.filter(email=email))== 0:
            ip, is_routable= get_client_ip(request)
        
                    
            if ip is None :
                    ip = '0.0.0.0'
            # else:
            #     if is_routable:
            #         ipv = 'Public'
            #     else:
            #         ipv = 'Private'
                    
            # print(ip, ipv)  
            
            try:
                response= DbIpCity.get(ip, api_key='free')
                country= response.country+'|'+response.city
            except:
                'Unknown Region'
            
            user = User.objects.create_user(username=uname, email=email, password=password)          
            b= Manager(name=name, uname=uname, email=email, ip=ip, country=country)
            b.save()
             
                
    
    return render(request, 'front/login.html')




def mylogout(request):
    
    logout(request)
    
    return redirect('mylogin')


def site_settings(request):
    
    #Login check starts Here:
    
    if not request.user.is_authenticated:
        
        return redirect('mylogin')
    #Login Check Ends Here
    
    
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1
    
    if prem == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})

    
    
    
    if request.method == 'POST':
        
        title= request.POST.get('title')
        body= request.POST.get('body')
        fb= request.POST.get('fb')
        tw= request.POST.get('tw')
        yt= request.POST.get('yt')
        ph= request.POST.get('ph')
        
        if fb== "" : fb= '#'
        if tw== "" : tw= '#'
        if yt== "" : yt= '#'
        
        if title== "" or body== "" or ph== "":
            error= 'All Fields are Required'
            return render(request, 'back/error.html', {'error':error})
        
        
        try:
            
            b= article.objects.get(pk=5)
            image = request.FILES['myfiles']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)
            
            picurl = url
            picname= filename
               
        except:     
            
            picurl= "-"
            picname= "-"
        
        try:
            
            b= article.objects.get(pk=5)
            image2 = request.FILES['myfiles2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(image2.name, image2)
            url2 = fs.url(filename2)
            
            picurl2 = url2
            picname2 = filename2
               
        
        except:     
            
            picurl2 = "-"
            picname2 = "-"
            
        b.title= title
        b.body= body
        b.fb= fb
        b.tw= tw
        b.yt= yt
        b.ph= ph
        b.picurl= picurl
        b.picname= picname
        b.picurl2 = picurl2
        b.picname2 = picname2        
        b.save() 
            
            
    site= article.objects.get(pk=5)     
    return render(request, 'back/settings.html', {'site':site})


def about_settings(request):
    
    #Login check starts here:
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login check ends here:
    
    
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1
    
    if prem == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})

    
    if request.method == 'POST':
        body= request.POST.get('aboutbody')
        if body == '':
            error= 'All Fields are Required'
            return render(request, 'back/error.html', {'error':error})
        
        v= article.objects.get(pk=5)
        v.bodylong= body
        v.save()
    
    
    aboutbody = article.objects.get(pk=5).bodylong
    
    return render(request, 'back/about_setting.html', {'aboutbody': aboutbody})



def contact(request):
    
    article_var=  article.objects.get(pk=5)
    news=  News.objects.all().order_by('-pk')
    cat= Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews=  News.objects.all().order_by('-pk')[:3]
    
    
    popularnews=  News.objects.all().order_by('-show')
    popularnews2=  News.objects.all().order_by('-show')[:3]
    
    trending= Trending.objects.all().order_by('-pk')[:5]
    
    return render(request, 'front/contact.html',{'name':article_var, 'News': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews, 'popularnews': popularnews, 'popularnews2':popularnews2, 'trending':trending })


def change_pass(request):
    
    #Login check starts here:
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login check ends here:
    
    if request.method == 'POST':
        
        oldpass= request.POST.get('oldpass')
        newpass= request.POST.get('newpass')
        
        if oldpass == "" or newpass == "":
            error = 'Wrong Password'
            return render(request, 'back/error.html', {'error':error})
        
        user= authenticate(username=request.user, password=oldpass)
        
        if user != None:
            
            if len(newpass) < 8:
                error = 'Password should be of atleast 8 Characters'
                return render(request, 'back/error.html', {'error':error})
            
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            for i in newpass:
                if i > '0' and i < '9':
                    count1 += 1
                if i > 'A' and i < 'Z':
                    count2 += 1
                if i > 'a' and i < 'Z':
                    count3 += 1
                if i > '!' and i < ')':
                    count4 += 1
            count = count1 + count2 + count3 + count4            
            if count >= 1:
                user= User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('mylogout') 
            
        else:
            error = 'Wrong Password'
            return render(request, 'back/error.html', {'error':error})    
    
    return render(request, 'back/changepass.html')


