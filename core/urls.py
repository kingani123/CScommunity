from operator import index
from django import views

from django.urls import include, path
from . import views
urlpatterns = [
      
       path('',views.index,name='index'), 
       path('setting',views.setting, name='setting'),
       path('upload',views.upload, name='upload'),
       path('like-post',views.like_post, name='like-post'),
       path('search', views.search, name='search'),
       path('comment', views.comment, name='comment'),
       path('pf',views.pf, name='pf'),
       path('pro',views.pro, name='pro'),
       path('signin',views.signin, name='signin'),
       path('logout',views.logout, name='logout'),
    
       path('code',views.code, name='code'),
       
       path('signup',views.signup,name='signup'),
      
       path('frequest',views.frequest, name='frequest'),
       path('accfrequest',views.accfrequest, name='accfrequest'),
       
      
       
       
    

      

      
       
    
]