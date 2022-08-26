from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('menupage/', views.move_to_menupage, name='move_to_menupage'),
    path('jikannwari/', views.move_to_jikannwari, name='move_to_jikannwari'),
    path('konnzatsu/', views.move_to_konnzatsu, name='move_to_konnzatsu'),
    path('syllabus/', views.move_to_syllabus, name='move_to_syllabus'),
    path('kyukou/', views.move_to_kyukou, name='move_to_kyukou'),
]
