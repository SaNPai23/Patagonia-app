from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    url(r'^edit/$', views.edit),
    url(r'^delete/$', views.delete),
    path('addpatient/', views.addpatient, name='addpatient'),
    # path('edit/', views.edit, name='edit'),

]
