from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
# Create your views here.
class SignupView(CreateView):
    # 使用するフォームを指定
    form_class = CustomUserCreationForm
    # 使用するテンプレートを指定
    template_name = 'signup.html'
    # 成功後のページを指定
    success_url = reverse_lazy('accounts:signup_success')

    # データベースに保存する関数
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'