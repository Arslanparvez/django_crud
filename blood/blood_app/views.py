from django.shortcuts import render,redirect
from .models import naya


# Create your views here.


def new(request):
    cc=naya.objects.all()
    c={}
    c['data']=cc
    return render(request,'new.html',c)
    

def old(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfiles=request.FILES['myfile']
        des=request.POST['upass']
        com=naya.objects.create(img=myfiles,description=des)
        return redirect('/show')
    else:
        return render(request,'old.html')
        

    
def deletepost(request,rid):
    oo=naya.objects.filter(id=rid)
    oo.delete()
    return redirect('/show')

def edit(request,pid):
    if request.method=='POST':
        des=request.POST['upass']
        
        cc=naya.objects.filter(id=pid)
        cc.update(description=des)
        # print(cc)
        return redirect('/show')
    else:

        dc=naya.objects.get(id=pid)
        c={}
        c['data']=dc
        return render(request,'getdata.html',c)

   

