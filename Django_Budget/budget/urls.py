from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-trans/', views.createTrans, name='create-trans'),
    path('delete-trans/<str:pk>/', views.deleteTrans, name='delete-trans'),
    path('add-pay/', views.add_pay, name='add-pay')
]
# <str:pk>/