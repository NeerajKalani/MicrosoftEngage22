from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from face_rec.views import EmailAttachementView

urlpatterns = [


	path('report/',views.report,name="report"),
	path('create_dataset', views.create_dataset,name="create_dataset"),
	path('trainer', views.trainer,name="trainer"),
	path('detect', views.TrackImages,name="detect"),
	path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
	path('report/',views.report,name="report"),
	path('profile/<str:pk>/', views.profile,name="profile"),
	path('all_students/', views.all_students,name="all_students"),
	path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
	path('absent_students/', views.absent_students,name="absent_students"),
	path('about/',views.about,name="about"),
	path('delete/<str:pk>',views.deleteStudent,name='delete'),
	path('register/', views.registerPage, name="register"),
	path('send/',views.send,name="send"),
	path('login/', views.loginPage, name="login"),   
	path('logout/', views.logoutUser,name="logout"),
	path('',views.loginPage),
	path('home/',views.home,name="home"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
	path('send_file/',views.send_file,name="send_file"),
    
	

]
