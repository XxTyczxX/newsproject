from django.urls import path
# ビューをインポート
from . import views

# 逆引きの設定
app_name = 'article'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateArticleView.as_view(), name='post'),
    path('post_success/', views.ArticleSuccessView.as_view(), name='post_done'),
    path('article/<int:category>/', views.CategoryView.as_view(), name='article_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),
    path('article-detail/<int:pk>/', views.DetailView.as_view(), name='article_detail'),
    path('mypage/', views.MypageView.as_view(), name = 'mypage'), 
    path('article-delete/<int:pk>/',views.ArticleDeleteView.as_view(),name = 'article_delete'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
