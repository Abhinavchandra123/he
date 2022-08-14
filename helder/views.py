import os
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
import datetime
from .models import Category,Photo

# from django.utils.datastructures import MultiValueDictKeyError


# login page
def loginadmin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=authenticate(request,username=uname,password=pwd)
        print(user,"hhh")
        if user:
            if user.is_staff==1:
                login(request,user)
                return redirect('adhome')
            
        # else:
        #     return render(request,'error.html')
    return render(request, "helderlogin.html")

# logout button
def logoutUser(request):
    logout(request)
    return redirect('login')

# addproduct page
@login_required(login_url='login')
def addPhoto(request):
    user = request.user
    
    categories = user.category_set.all()

    # try:
    #     imgname = request.POST['imgname']
    # except MultiValueDictKeyError:
    #     imgname = False

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        
        date = datetime.datetime.now()#.strftime('%H:%M:%S')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
            name=category
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
                
            name=data['category_new']  
        else:
            category = None
        photo = Photo.objects.create(
            category=category,
            name=name,
            date=date,
            size=data['size'],
            imgname=data['imgname'],
            description=data['description'],
            detail1=data['fabric'],
            detail2=data['type'],
            detail3=data['pattern'],
            detail4=data['dtls4'],
            detail5=data['dtls5'],
            image=image,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
        )

        return redirect('addph')

    context = {'categories': categories}
    return render(request, 'helderadd.html', context)

    #admin home view
@login_required(login_url='login')
def adminhome(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photo = Photo.objects.filter(category__user=user)
    else:
        photo = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    photos=photo.order_by('-date')
    context = {'categories': categories, 'photos': photos}
    return render(request, 'adminhome.html', context)


def delb(request,id):
    
    bks=Photo.objects.get(id=id)
    os.remove(bks.image.path)
    os.remove(bks.image1.path)
    os.remove(bks.image2.path)
    os.remove(bks.image3.path)
    os.remove(bks.image4.path)
    
    bks.delete()
    

    return redirect("adhome")

    #edit page
@login_required(login_url='login')
def form2Photo(request,pk):
    # user = request.user
    photos = Photo.objects.get(id=pk)

    # categories = user.category_set.all()
    if request.method=="GET":
        photos = Photo.objects.get(id=pk)
        context = {}
        context['data']=photos
        return render(request,'helderedit.html',context)
    elif request.method=="POST":
        #   #for image edit

        data = request.POST
        date = datetime.datetime.now()
        name1=photos.name

        if request.FILES.get('image')!=None:
            image = request.FILES.get('image')
            os.remove(photos.image.path)
        else:
            image=photos.image
        if request.FILES.get('image1')!=None:
            image1 = request.FILES.get('image1')
            os.remove(photos.image1.path)
        else:
            image1=photos.image1
        if request.FILES.get('image2')!=None:
            image2 = request.FILES.get('image2')
            os.remove(photos.image2.path)
        else:
            image2=photos.image2
        if request.FILES.get('image3')!=None:
            image3 = request.FILES.get('image3')
            os.remove(photos.image3.path)
        else:
            image3=photos.image3
        if request.FILES.get('image4')!=None:
            image4 = request.FILES.get('image4')
            os.remove(photos.image4.path)
        else:
            image4=photos.image4


        Photo.objects.create( 
            category=photos.category,
            imgname=data['imgname'],
            name=name1,
            description=data['description'],
            date=date,
            size=data['size'],
            detail1=data['fabric'],
            detail2=data['type'],
            detail3=data['pattern'],
            detail4=data['dtls4'],
            detail5=data['dtls5'],
            image=image,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
            )
        bks=Photo.objects.get(id=pk)
        bks.delete()

        return redirect('adhome')

def product(request):
    user = request.user
    category = request.GET.get('category')
    categories = Category.objects.all()
    photos=Photo.objects.all().order_by('-date')
    context = {'categories': categories, 'photos': photos}
    return render(request, 'products.html', context)


def index(request):
    
    category = request.GET.get('category')
    categories = Category.objects.all()
    photos = Photo.objects.all().order_by('-date')
    context = {'categories': categories, 'photos': photos}
    return render(request, 'index.html', context)