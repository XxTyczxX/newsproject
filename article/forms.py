from django.forms import ModelForm
from .models import ArticlePost
from django import forms

class ArticlePostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = ArticlePost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

class ContactForm(forms.Form):
    # HTML側のデータを取得
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label= 'メッセージ', widget=forms.Textarea)

    # __init__メソッド ⇒ 初期化メソッド
    def __init__(self, *args, **kwargs):

        
        super(). __init__(*args, **kwargs)
        #name フィールドのplaceholderにメッセージを登録
        self.fields['name'].widget.attrs['placeholder'] = \
        'お名前を入力してください'
        #name フィールドを出力する <input>タグのclass 属性を設定
        self.fields['name'].widget.attrs['class'] = 'form-control'

        # email フィールドのplaceholderにメッセージを登録
        self.fields['email'].widget.attrs['placeholder'] = \
        'メールアドレスを入力してください'
        #email フィールドを出力する <input > タグのclass 属性を設定
        self.fields['email'].widget.attrs['class'] = 'form-control'

        # message フィールドのplaceholderにメッセージを登録
        self.fields['message'].widget.attrs['placeholder'] = \
        'メッセージを入力してください'
        # message フィールドを出力する <input> タグのclass 属性を設定
        self.fields['message'].widget.attrs['class'] = 'form-control'


