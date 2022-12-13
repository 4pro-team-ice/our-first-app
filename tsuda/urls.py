from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # ログイン機能用のURL
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    # path("home",views.home,name="home"),

    #時間割登録用のURL
    path('jikannwari/term1', views.t1_list, name='t1_list'),
    path('jikannwari/term1/post/<int:pk>/', views.t1_detail, name='t1_detail'),
    path('jikannwari/term1/new/', views.t1_new, name='t1_new'),
    path('jikannwari/term1/post/<int:pk>/edit/', views.t1_edit, name='t1_edit'),

    path('jikannwari/term2', views.t2_list, name='t2_list'),
    path('jikannwari/term2/post/<int:pk>/', views.t2_detail, name='t2_detail'),
    path('jikannwari/term2/new/', views.t2_new, name='t2_new'),
    path('jikannwari/term2/post/<int:pk>/edit/', views.t2_edit, name='t2_edit'),

    path('jikannwari/term3', views.t3_list, name='t3_list'),
    path('jikannwari/term3/post/<int:pk>/', views.t3_detail, name='t3_detail'),
    path('jikannwari/term3/new/', views.t3_new, name='t3_new'),
    path('jikannwari/term3/post/<int:pk>/edit/', views.t3_edit, name='t3_edit'),

    path('jikannwari/term4', views.t4_list, name='t4_list'),
    path('jikannwari/term4/post/<int:pk>/', views.t4_detail, name='t4_detail'),
    path('jikannwari/term4/new/', views.t4_new, name='t4_new'),
    path('jikannwari/term4/post/<int:pk>/edit/', views.t4_edit, name='t4_edit'),

    #シラバスコメント用のURL
    path('syllabus/', views.syllabuscomment_list, name='syllabuscomment'),
    path('syllabus/post/<int:pk>/', views.syllabuscomment_detail, name='syllabuscomment_detail'),
    path('syllabus/new/', views.syllabuscomment_new, name='syllabuscomment_new'),
    path('syllabus/post/<int:pk>/edit/', views.syllabuscomment_edit, name='syllabuscomment_edit'),

    #シラバス検索用のURL
    path('syllabuskekka/', views.syllabuskekka_list, name='syllabuskekka'),
    path('syllabuskensaku/', views.move_to_syllabuskensaku, name='move_to_syllabuskensaku'),
    path('syllabuskekka/post/<int:pk>/', views.syllabus_detail, name='syllabus_detail'),#科目名を押すと飛ぶ
    path('syllabuskekka/', views.move_to_syllabuskekka, name='move_to_syllabuskekka'),
    path('syllabuskamoku/', views.move_to_syllabuskamoku, name='move_to_syllabuskamoku'),
    path('syllabuswordcloud/', views.move_to_syllabuswordcloud, name='move_to_syllabuswordcloud'),
    path('syllabuswordcloud/wordcloud/<int:pk>/', views.syllabus_wordcloud, name='syllabus_wordcloud'),#科目名を押すと飛ぶ


    path('menupage/', views.move_to_menupage, name='move_to_menupage'),
    path('jikannwari/', views.move_to_jikannwari, name='move_to_jikannwari'),
    path('jikannwari/term/', views.move_to_jikannwari_term, name='move_to_jikannwari_term'),
    path('akikyoshitsu/', views.move_to_akikyoshitsu, name='move_to_akikyoshitsu'),
    path('akikyoshitsukekka/', views.akikyoshitsu_list, name='akikyoshitsukekka'),
    path('akikyoshitsukekka/', views.move_to_akikyoshitsukekka, name='move_to_akikyoshitsukekka'),


    path('syllabus/', views.move_to_syllabus, name='move_to_syllabus'),
    path('map/', views.move_to_map, name='move_to_map'),
    path('eigyoujikan/', views.move_to_eigyoujikan, name='move_to_eigyoujikan'),
    path('jihanki/', views.move_to_jihanki, name='move_to_jihanki'),



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
