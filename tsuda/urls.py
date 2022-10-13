from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    #時間割登録用のURL
    path('jikannwari/', views.monday1_list, name='monday1'),
    path('jikannwari/post/<int:pk>/', views.monday1_detail, name='monday1_detail'),
    path('jikannwari/new/', views.monday1_new, name='monday1_new'),
    path('jikannwari/post/<int:pk>/edit/', views.monday1_edit, name='monday1_edit'),

    #シラバスコメント用のURL
    path('syllabus/', views.syllabuscomment_list, name='syllabuscomment'),
    path('syllabus/post/<int:pk>/', views.syllabuscomment_detail, name='syllabuscomment_detail'),
    path('syllabus/new/', views.syllabuscomment_new, name='syllabuscomment_new'),
    path('syllabus/post/<int:pk>/edit/', views.syllabuscomment_edit, name='syllabuscomment_edit'),



    path('menupage/', views.move_to_menupage, name='move_to_menupage'),
    path('jikannwari/', views.move_to_jikannwari, name='move_to_jikannwari'),
    path('akikyoshitsu/', views.move_to_akikyoshitsu, name='move_to_akikyoshitsu'),
    path('akikyoshitsukekka/', views.move_to_akikyoshitsukekka, name='move_to_akikyoshitsukekka'),
    path('syllabus/', views.move_to_syllabus, name='move_to_syllabus'),
    path('map/', views.move_to_map, name='move_to_map'),
    path('eigyoujikan/', views.move_to_eigyoujikan, name='move_to_eigyoujikan'),
    path('jihanki/', views.move_to_jihanki, name='move_to_jihanki'),

    path('syllabuskensaku/', views.move_to_syllabuskensaku, name='move_to_syllabuskensaku'),
    path('syllabuskekka/', views.move_to_syllabuskekka, name='move_to_syllabuskekka'),
    path('syllabuskamoku/', views.move_to_syllabuskamoku, name='move_to_syllabuskamoku'),
    path('syllabuswordcloud/', views.move_to_syllabuswordcloud, name='move_to_syllabuswordcloud'),

    path('honkan/', views.move_to_honkan, name='move_to_honkan'),
    path('shinkan/', views.move_to_shinkan, name='move_to_shinkan'),
    path('minami/', views.move_to_minami, name='move_to_minami'),
    path('tokkyo/', views.move_to_tokkyo, name='move_to_tokkyo'),
    path('ichigokan/', views.move_to_ichigokan, name='move_to_ichigokan'),
    path('gogokan/', views.move_to_gogokan, name='move_to_gogokan'),
    path('nanagokan/', views.move_to_nanagokan, name='move_to_nanagokan'),
    path('library/', views.move_to_library, name='move_to_library'),
    path('shokudo/', views.move_to_shokudo, name='move_to_shokudo'),
]
