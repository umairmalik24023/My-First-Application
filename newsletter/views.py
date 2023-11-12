from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import datetime
import news
from .models import Newsletter
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User , Group, Permission
from django.contrib.contenttypes.models import ContentType



def news_letter(request):
    
    if request.method == 'POST':
        txt = request.POST.get('txt')
        result = txt.find('@')
        if int(result) != -1:
            b =  Newsletter(txt=txt, status=1)
            b.save()
        else:
            try:
                int(txt)
                b = Newsletter(txt=txt, status=2)
                b.save()
            except:
                return redirect('home')



    return redirect('home')

def news_emails(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    emails = Newsletter.objects.filter(status=1)


    return render(request,'back/emails.html',{'emails':emails})




def news_phones(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    phones = Newsletter.objects.filter(status=2)


    return render(request,'back/phones.html',{'phones': phones})




def news_txt_del(request, id, name):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    b = Newsletter.objects.filter(pk=id)
    b.delete()
    if int(name) == 2:
        return redirect('news_phones')

    return redirect('news_emails')

