from django.urls import path
from .views import index,sair

urlpatterns = [

    path('', index, name='index'),
    path('logout/', sair, name='sair')

]