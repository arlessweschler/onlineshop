from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.to_profile, name='login'),
    path('logout/', views.profile_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_change/', views.profile_change, name='profile_change'),
    path('password_change/', PasswordChangeView.as_view(template_name='accounts/password_change_form.html',
                                                        success_url = reverse_lazy ('accounts:password_change_done')),
                                                        name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='accounts/password_changed.html'),
                                                                 name='password_change_done'),
    path('registration/', views.registration , name='registration'),
]