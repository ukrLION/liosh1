from django.urls import path


from . import views

urlpatterns = [
    path('<path:var>', views.index, name='index'),
    path('',views.index, name='index')
]
