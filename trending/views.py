from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.

from .models import Trending
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat
from myapp.models import article


def trending_add(request):
    
    #Login check starts here:
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login check ends here:

    if request.method == 'POST':                   #Section to add data into database
        
        trend= request.POST.get('trending')
        if trend == "":
            error= 'All Fields are Required'
            return render(request, 'back/error.html', {'error':error})
        b= Trending(headline=trend)
        b.save()
        
    trending= Trending.objects.all()
        
    
    return render(request, 'back/trending.html', {'trending': trending})

def trending_del(request, id):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    b = Trending.objects.filter(pk=id)
    b.delete()

    return redirect('trending_add')


def trending_edit(request, id):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    myheadline = Trending.objects.get(pk=id).headline

    if request.method == 'POST':
        headline = request.POST.get('headline')
        if headline == "":
            error = "All fields are required"
            return render(request,'back/error.html', {'error':error})
        b = Trending.objects.get(pk=id)
        b.headline = headline
        b.save()
        return redirect('trending_add')



    return render(request, 'back/trending_edit.html',{'myheadline':myheadline, 'id':id})





