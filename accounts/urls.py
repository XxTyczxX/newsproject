from django.urls import path
# ビューをインポート
from . import views
# ログイン専用のビューをインポート()
from django.contrib.auth import views as auth_views

# 逆引きの設定
app_name = 'accounts'

urlpatterns = [
    # サインアップページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # viewsモジュールのSignUpViewをインスタンス化する
    path('signup/', views.SignupView.as_view(), name='signup'),

    # サインアップ完了ページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup_success/」へのアクセスに対して、
    # viewsモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),

    # ログインページの表示
    # 「http(s)://<ホスト名>/login/」へのアクセスに対して、
    # django.contrib.auth.views.LoginViewをインスタンス化して
    # ログインページを表示する
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # ログアウトを実行
    # 「http(s)://<ホスト名>/logout/」へのアクセスに対して、
    # django.contrib.auth.views.LogoutViewをインスタンス化して
    # ログアウトさせる
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
