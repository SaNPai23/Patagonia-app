from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

]
