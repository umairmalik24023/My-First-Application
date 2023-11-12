from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import datetime
import news
from .models import Contactform
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
import datetime
from django.contrib.auth import authenticate,login,logout


def contact(request):
    
    article_var=  article.objects.get(pk=5)
    news=  News.objects.all().order_by('-pk')
    cat= Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews=  News.objects.all().order_by('-pk')[:3]
    
    
    popularnews=  News.objects.all().order_by('-show')
    popularnews2=  News.objects.all().order_by('-show')[:3]
    
    trending= Trending.objects.all().order_by('-pk')
    
    return render(request, 'front/contact.html',{'name':article_var, 'News': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews, 'popularnews': popularnews, 'popularnews2':popularnews2, 'trending':trending })




def contact_add(request):
    
    now= datetime.datetime.now()
    year= now.year
    month= now.month
    day= now.day
    if (len(str(day)))==1:
        day= '0' +str(day)
    if (len(str(month)))==1:
        month= '0' +str(month)
    date = str(year)+'-'+ str(month)+'-'+str(day)
    time = str(now.hour)+'-'+ str(now.minute)
    
    
    
    
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        body= request.POST.get('body')
        
        if name == '' or email == '' or body == '':
            msg= 'Please fill all the body'
            return render(request, 'front/message.html', {'msg':msg})
        
        b= Contactform(name=name, email=email, body=body, date=date, time=time)
        b.save()
        msg= 'Thanks for contacting us, WE will get back to you as soon as possible'  
        return render(request, 'front/message.html', {'msg':msg})    
    
    return render(request, 'front/message.html')



def contact_show(request):
    
    #Login check starts here:
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login check ends here:
    
    msg= Contactform.objects.all()
    
    
    
    return render(request,  'back/contact_form.html', {'msg':msg})


def contact_del(request, id):
    
    #Login check starts here:
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login check ends here:
    
    b= Contactform.objects.get(pk=id)
    b.delete()
    
    return redirect('contact_show')



