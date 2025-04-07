from django.contrib import admin
from .models import Command, Friend, CommandRecipient  

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'command_number', 'status', 'scheduled_time','created_at')  # 목록에서 보여줄 필드
    list_filter = ('status', 'created_at')  # 필터 사이드바
    search_fields = ('user__username', 'recipients__username', 'message')  # 검색
    # filter_horizontal = ('recipients',)  # recipients 필드를 가로 ManyToMany 선택창으로 표시

    # scheduled_time = models.DateTimeField(null=True, blank=True)  # ✅ 이 줄 추가!


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'image_url', 'created_at')  # 목록에 보여줄 컬럼
    list_filter = ('user', 'created_at')  # 필터 사이드바
    search_fields = ('user__username', 'name')  # 검색 기능

    

@admin.register(CommandRecipient)
class CommandRecipientAdmin(admin.ModelAdmin):
    list_display = ('command', 'friend', 'status', 'sent_at')
    list_filter = ('status',)
    search_fields = ('command__message', 'friend__name')
    