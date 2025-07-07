from django.urls import path

from .views import *
urlpatterns=[
    # path('', camera_list, name='cameras'),
    path('', CamerasList.as_view(), name='cameras'),

    # path('camera_detail/<int:pk>', camera_detail, name='camera_detail'),
    path('camera_detail/<int:pk>', CamerasDetail.as_view(), name='camera_detail'),
    # path('update/<int:pk>', update_camera, name='update_camera'),
    path('update/<int:pk>', CameraUpdate.as_view(), name='update_camera'),

    # path('del_camera/<int:pk>', delete_camera, name='delete_camera'),
    path('del_camera/<int:pk>', CamerasDelete.as_view(), name='delete_camera'),
    # path('create/', create_camera, name="create_camera")
    path('create/', CamerasCreate.as_view(), name="create_camera")
]