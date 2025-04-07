from django.urls import path
from .views import about_view,create_command, CustomLoginView, add_friend,signup_view ,api_friends
from django.views.generic import TemplateView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('about/', about_view, name='about'),
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('friends/add/', add_friend, name='add_friend'),
    path('friends/load/', TemplateView.as_view(template_name='friends/load_friend.html'), name='load_friend'),
    path('command/new/', create_command, name='create_command'),
    path('api/friends/', api_friends, name='api_friends'),
    path('command/success/', TemplateView.as_view(template_name='commands/command_success.html'), name='command_success'),
    

]