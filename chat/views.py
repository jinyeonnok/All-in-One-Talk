from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommandForm, KoreanLoginForm, FriendAddForm
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Friend
from django.http import JsonResponse


def about_view(request):
    return render(request, 'about.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 회원가입 후 로그인 페이지로 이동
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'  # 📌 새로운 템플릿 경로 지정
    
    authentication_form = KoreanLoginForm  # ✅ 여기 적용!




@login_required
def create_command(request):
    if request.method == 'POST':
        form = CommandForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            command = form.save(commit=False)
            command.user = request.user
            command.status = 'pending'
            command.save()
            form.save_m2m()  # recipients 저장
            return redirect('command_success')  # 저장 후 이동할 페이지
    else:
        form = CommandForm(user=request.user)

    return render(request, 'commands/create_command.html', {'form': form})


@login_required
def api_friends(request):
    user = request.user
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 50))
    search = request.GET.get('search', '')

    friends = Friend.objects.filter(user=user)
    if search:
        friends = friends.filter(name__icontains=search)

    friends = friends.order_by('name')[offset:offset + limit]

    data = [{
        'id': f.id,
        'name': f.name,
        'image_url': f.image_url or ''
    } for f in friends]

    return JsonResponse({'friends': data})

@login_required
def add_friend(request):
    if request.method == 'POST':
        # 삭제 요청인지 확인
        if 'delete' in request.POST:
            friend_id = request.POST.get('friend_id')
            Friend.objects.filter(id=friend_id, user=request.user).delete()
            return redirect('add_friend')

        # 추가 요청 처리
        form = FriendAddForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.user = request.user
            friend.save()
            return redirect('add_friend')
    else:
        form = FriendAddForm()

    # 내 친구 목록
    my_friends = request.user.my_friends.all()

    return render(request, 'friends/add_friend.html', {
        'form': form,
        'friends': my_friends
    })

