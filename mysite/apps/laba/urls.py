from django.urls import path     #   /sometext
from django.urls import re_path  #   /^regular$

from . import views

urlpatterns = [
	path('test/',views.test,name="test"),
    path('test/<str:var>/', views.test, name='test'),
    
    #path('<str:link>/',views.test, name='test'),       ##     or <int:link> or <str:> ...
    path('unit', views.unit, name='unit'),
    path('9/',views.ninth, name='ninth'),
    path('8/',views.eighth, name='eighth'),
    path('7/',views.seventh, name='seventh'),
    path('6/',views.sixth, name='sixth'),
    path('5/',views.fifth, name='fifth'),
    path('4/',views.fourth, name='fourth'),
    path('3/',views.third, name='third'),
    path('2/',views.second, name='second'),
    path('1/',views.first, name='first'),
    
    path('',views.index,name='index') # match with everything
    ]


"""
<спецификаторы:параметр>
str: соответствует любой строке за исключенем символа "/". Если спецификатор не указан, то используется по умолчанию
int: соответствует любому положительному числу
slug: соответствует последовательности буквенных символов ASCII, цифр, дефиса и символа подчеркивания, например, building-your-1st-django-site
uuid: сооветствует идентификатору UUID, например, 075194d3-6885-417e-a8a8-6c931e272f00
path: соответствует любой строке, которая также может включать символ "/" в отличие от спецификатора str

"""

