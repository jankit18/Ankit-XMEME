from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import ContentImage
# Create your views here.

def Content(request):
    if request.method == "POST":
        userName = request.POST['Name']
        imageUrl = request.POST['ImageUrl']
        caption = request.POST['Caption']
        
        if len(userName)==0 or len(imageUrl)==0 or len(caption)==0 :
            messages.info(request,'Post Unsuccessfully Some Field is Empty !')
            print("chitya")
            return redirect('contentPage')


        if ContentImage.objects.filter(name=userName,caption=caption,url=imageUrl).exists():
            messages.info(request,'Post Already Exist')
            return redirect('contentPage')
        else:
            try:
                post = ContentImage.objects.create(name=userName,url=imageUrl,caption=caption)
                post.save()
                messages.info(request,'Posted Successfully')
            except:
                messages.info(request,'Post Unsuccessfully Try Again!')
            return redirect('contentPage')
    else:
        return render(request,'XMEME.html')