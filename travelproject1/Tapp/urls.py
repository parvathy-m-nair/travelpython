
from django.urls import path
from.import views

urlpatterns = [

    path('',views.view_items,name='view_items')

]


