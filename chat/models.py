import uuid
from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_friends')
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)  # ✅ 추가
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} : {self.name}"

class Command(models.Model):
    STATUS_CHOICES = [
        ('pending', '대기 중'),
        ('processing', '처리 중'),
        ('completed', '완료됨'),
        ('failed', '실패'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    command_number = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='commands/images/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    scheduled_time = models.DateTimeField(null=True, blank=True)  # ✅ 이 줄 추가!
    created_at = models.DateTimeField(auto_now_add=True)

    recipients = models.ManyToManyField(Friend, through='CommandRecipient', related_name='commands')
    # recipients = models.ManyToManyField(Friend, related_name='commands')  # ✅ Friend로 변경

    def save(self, *args, **kwargs):
        if not self.command_number:
            last_command = Command.objects.filter(user=self.user).order_by('-command_number').first()
            self.command_number = (last_command.command_number + 1) if last_command else 1
        super().save(*args, **kwargs)

    def __str__(self):
        friend_names = [f.name for f in self.recipients.all()]
        return f"#{self.command_number} {self.user.username} → {friend_names}: {self.message or '사진 첨부'}"

class CommandRecipient(models.Model):
    STATUS_CHOICES = [
        ('pending', '대기 중'),
        ('processing', '처리 중'),
        ('completed', '완료됨'),
        ('failed', '실패'),
    ]

    command = models.ForeignKey('Command', on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    error_message = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('command', 'friend')

    def __str__(self):
        return f"{self.command} → {self.friend.name} ({self.status})"
