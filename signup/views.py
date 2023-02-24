from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import Artist,Work,Client

@login_required(login_url='loggedin')
def api(request):
    return render(request,'api.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        

        my_user=User.objects.create_user(username,email,password)
        my_user.save()
        return redirect('loggedin')
        

    return render(request,'signin.html')

def loggedin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('api')

        else:
            return HttpResponse('Username or pass is incorrect')


    return render(request,'login.html')

def loggedout(request):
    logout(request)
    return redirect('loggedin')
    

def search(request):
    
    srch= request.POST.get('srch', '')
    artist= Artist.objects.filter(name=srch)
    print(artist)
    if artist.exists():
        return render(request, 'artist.html',{'artist': artist[0], 'art':srch})
    else:
        return HttpResponse('sorry could not find artist')
    


def filter(request):
    
    flt= request.POST.get('flt', '')
    artist= Artist.objects.filter(work__work_type=flt)
    print(artist)
    if artist.exists():
        return render(request, 'filter.html',{'artist': artist[0:], 'art':flt})
    else:
        return HttpResponse('sorry could not find artist with filter')
    



    
        
