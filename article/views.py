from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ArticlePostForm
from .models import ArticlePost
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

class IndexView(ListView):
    """トップページのビュー"""
    template_name = 'index.html'
    queryset = ArticlePost.objects.order_by('-posted_at') 
    paginate_by = 9
    

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('article:contact')

    def form_valid(self, form):
        # フォームに入力されたデータをフィールド名を指定して取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']


        # フォームの入力データの書式を設定
        ### 本文 ###
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ: {2}\n '.format(name, email, message)

        # 送信元のメールアドレス
        from_email = 'admin@example.com'
        # 送信先のメールアドレス
        to_email = ['admin@example.com']

        ### ↑↑ 送信するための準備完了 ### 
        
        # EmailMessage オブジェクトを生成
        message = EmailMessage(body=message, from_email=from_email, to=to_email)
        # メッセージを送信(上記で作成したオブジェクトのメソッドを呼び出し)
        message.send()

        # 送信完了後に表示するメッセージ
        messages.success(self.request, 'お問い合わせは正常に送信されました。')

        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CreateArticleView(CreateView):
    """ニュース記事投稿ページのビュー"""
    form_class = ArticlePostForm
    template_name = "post_article.html"
    success_url = reverse_lazy('article:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class ArticleSuccessView(TemplateView):
    """投稿完了ページのビュー"""
    template_name = 'post_success.html'

class CategoryView(ListView):
    """カテゴリごとの記事一覧ページのビュー"""
    template_name = 'index.html'  
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category'] 

        return ArticlePost.objects.filter(category=category_id).order_by('-posted_at')

class UserView(ListView):
    '''ユーザーの投稿一覧ページのビュー

    Attributes:
    template_name: レンダリングするテンプレート
    paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        '''クエリを実行する

        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する

        Returns:
        クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # userキーの値(ユーザーテーブルのid)を取得
        user_id = self.kwargs['user']
        # filter(フィールド名=id)で絞り込む
        user_list = ArticlePost.objects.filter(
            user=user_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return user_list

class MypageView(ListView):
    # HTMLを指定
    template_name ='mypage.html'
    # ページネーションを指定(9)
    paginate_by = 9

    def get_queryset(self):
        # ログインしているユーザで絞込
        # PhotoPostモデルから
        queryset = ArticlePost.objects.filter(user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return queryset

class DetailView(DetailView):
    """記事の詳細表示ビュー"""
    template_name = 'detail.html'
    model = ArticlePost

@method_decorator(login_required, name='dispatch')
class MypageView(ListView):
    """マイページのビュー"""
    template_name = 'mypage.html'

    def get_queryset(self):
        return ArticlePost.objects.filter(user=self.request.user).order_by('-posted_at')

@method_decorator(login_required, name='dispatch')
class ArticleDeleteView(DeleteView):
    """記事削除のビュー"""
    model = ArticlePost
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article:mypage')

