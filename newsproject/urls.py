from django.contrib import admin
from django.urls import include, path
# auth.viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views
# settingsを追加
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls')),
    path('', include('accounts.urls')),

    # パスワードリセットのためのURLパターン
    # メアドに送られるとURLとなる
    # 毎回異なり、自動生成され一回限り有効なURL(Djangoの機能を使用する)
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = "password_reset.html"),name ='password_reset'),
    
    # メール送信完了ページ
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"),name ='password_reset_done'),
    
    # パスワードリセットページ
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"),name ='password_reset_confirm'),
    
    # パスワードリセット完了ページ
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"),name ='password_reset_complete'),
]

urlpatterns += static(

    settings.MEDIA_URL,

    document_root=settings.MEDIA_ROOT
)
