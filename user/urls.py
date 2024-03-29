from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 회원가입
    path('signup/', views.SignupView.as_view(), name='signup'),
    # 회원탈퇴
    path('signout/', views.SignoutView.as_view(), name='signout'),
    # 로그인
    path('login/', views.LoginView.as_view(), name='login'),
    # 로그아웃
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # 회원정보 조회
    path('profile/<int:user_id>', views.ProfileView.as_view(), name='profile'),
    # 회원정보 수정
    path('update/', views.UserUpdateView.as_view(), name='user-update'),
]
