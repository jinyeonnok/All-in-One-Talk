from django import forms
from .models import Command, Friend
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일 주소를 입력하세요'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CommandForm(forms.ModelForm):
    scheduled_time = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'id': 'id_scheduled_time'
            }
        )
    )

    class Meta:
        model = Command
        fields = ['message', 'image', 'recipients', 'scheduled_time']  # ✅ 필드에 추가
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'recipients': forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'recipients'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['recipients'].queryset = Friend.objects.filter(user=user)

class KoreanLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _("아이디 또는 비밀번호가 올바르지 않습니다."),
        'inactive': _("이 계정은 비활성화되어 있습니다."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class FriendAddForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '친구 이름을 입력하세요'
            })
        }

