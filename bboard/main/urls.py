from django.urls import path
from .views import index
from .views import other_page

from .views import RegisterUserView, RegisterDoneView
from .views import BBPasswordChangeView
from .views import ChangeUserInfoView
from .views import BBLogoutView
from .views import profile
from .views import BBLoginView
from .views import user_activate

app_name = 'main'

urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_active'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('account/register/', RegisterUserView.as_view(), name='register'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('', index, name='index')
]