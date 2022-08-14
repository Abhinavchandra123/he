from itertools import product
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',loginadmin, name="login"),
    path('logout/',logoutUser, name="logout"),
    # path('register/', views.registerUser, name="register"),
    path('adminhome/', adminhome, name='adhome'),
    path('addproduct/',addPhoto, name='addph'),
    path('product/',product, name='pdct'),
    
    # path('',index, name='ind'),
    # path('old/',product, name='pdct'),
    path('delb/<id>',delb,name="delb"),
    path('productedit/<str:pk>/',form2Photo, name='edit'),
]