from django.urls import path

from .views import *
urlpatterns=[
    path('', camera_list, name='cameras'),
    path('camera_detail/<int:pk>', camera_detail, name='camera_detail'),
    path('update_camera/<int:pk>', update_camera, name='update_camera'),
    path('del_camera/<int:pk>', delete_camera, name='delete_camera'),
    path('create/', create_camera, name="create_camera")
]