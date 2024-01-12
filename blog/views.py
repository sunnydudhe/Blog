from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,get_object_or_404
from .form import newpost,profilepage,commet
from . models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.contrib import messages






def home(request):
    all_posts = post.objects.all().order_by('-date')
    categori = categories.objects.all()
    catego = request.GET.get('category')
    if catego:
        all_posts = all_posts.filter(category__cate=catego)
    per_page = 4
    page_number = request.GET.get('page')
    paginator = Paginator(all_posts, per_page)
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'data': page, 'c': categori})

def SignupPage(request):
    if request.method=='POST':    
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if not uname or not email or not pass1:
            return HttpResponse("<a href='/signup'>Please fill in all the required fields.</a> ")

        if pass1!=pass2:
            return HttpResponse(" <a href='/signup'>Your password and confrom password are not Same!</a> ")
        
        if User.objects.filter(email=email).exists():
            return HttpResponse("<a href='/signup'>A user with this email already exists. Please use a different email address.</a>")
        elif User.objects.filter(username=uname).exists():
            return HttpResponse("<a href='/signup'>This username is already taken. Please choose a different username.</a>")
        else:
            User.objects.create_user(uname,email,pass1)
            return redirect('/login')
    return render (request,'signup.html')

  
    
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/profile')
        
        elif not username or not password:
            return HttpResponse("Please fill in all the required fields.<a href='/login'>Go Back</a> ")
        else:
            return HttpResponse("username and password dosent match <a href='/login'>Go Back</a> ")
    return render(request,'login.html')

@login_required(login_url="/login")
def pagelogout(request):
    logout(request)
    return redirect('/home')



@login_required(login_url="/login")
def postdata(request):
    if request.method == 'POST':
        postform=newpost(request.POST,request.FILES)
        if postform.is_valid():
            data=postform.save(commit=False)
            data.author = request.user
            data.save()
            return redirect('/profile')
    else:
        postform=newpost()
    return render(request,'post.html',{'bpost':postform})

@login_required(login_url="/login")
def profilehome(request):
    user = request.user
    posts = post.objects.filter(author=user).order_by('-date') 
    return render(request, 'profile.html', {'u': user, 'p': posts})


@login_required(login_url="/login")
def updatedata(request,id):
    uss=post.objects.get(id=id)
    ff=newpost(instance=uss)
    if request.method=='POST':
        ff=newpost(request.POST,request.FILES,instance=uss)
        if ff.is_valid():
            ff.save()
            return redirect('/profile')
    return render(request,'update.html',{'ff':ff})    


@login_required(login_url="/login")
def deletfun(request,id):
    data=post.objects.get(id=id)
    data.delete()
    return redirect('/profile')

@login_required(login_url="/login")
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form =profilepage(request.POST,request.FILES ,instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/pro')
    else:
        form = profilepage(instance=user_profile)
    return render(request, 'profilepage.html', {'form': form})




@login_required(login_url="/login")
def alldata(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except ObjectDoesNotExist:
        profile = None     

    return render(request, 'protem.html', {'user': user, 'profile': profile})


def add_comment(request, id):
    ppost = get_object_or_404(post, id=id)

    if request.method == 'POST':
        data = commet(request.POST)
        if data.is_valid():
            comment = data.save(commit=False)
            comment.blog_post = ppost
            comment.save()
            return redirect('/home')      

    else:
        data = commet()
    return render(request, 'coment.html', {'post': ppost,'data':data})


def pro(request, author):
    try:
        ppost = UserProfile.objects.get(user__username=author)
    except ObjectDoesNotExist:
        ppost=None
    return render(request, 'ppp.html', {'po': ppost})



def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        if not name or not email or not message:
            return HttpResponse("Please fill in all the required fields.<a href='/contact'>Go Back</a> ")
        else:
            data=ContactMessage.objects.create(name=name,email=email,message=message)
            data.save()
            return HttpResponse("success <a href='/home'>Go Back</a>")

    return render(request,'contact.html')

def fullp(request,id):
    data=post.objects.get(id=id)
    return render(request,'fullpost.html',{'d':data})