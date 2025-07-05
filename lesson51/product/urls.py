from django.urls import path

from .views import *
urlpatterns=[
    path('', conditioner_list, name='conditioners'),
    path('conditioner_detail/<int:pk>', conditioner_detail, name='conditioner_detail'),
    path('update_conditioner/<int:pk>', update_conditioner, name='update_conditioner'),
    path('del_conditioner/<int:pk>', delete_conditioner, name='delete_conditioner'),
    path('create/', create_conditioner, name="create_conditioner")
]