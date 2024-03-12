# pages/urls.py
from django.urls import path

from .views import home_page_view, signup, login_view, welcome

urlpatterns = [
    path("", home_page_view, name="home"),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('welcome/', welcome, name='welcome')
]
