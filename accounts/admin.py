from django.contrib import admin
#CustomUser をインポート
from .models import CustomUser

from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin (admin. ModelAdmin):
    # 管理ページのレコード一覧に表示するカラムを設定するクラス
    #レコード一覧にidとusername を表示
    list_display = ('id', 'username')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'username')

# Django管理サイトにCustomUser, CustomUserAdminを登録する
admin.site.register(CustomUser, CustomUserAdmin)