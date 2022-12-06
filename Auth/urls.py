from django.urls import path
from .views import log_in,register, log_out
from Quiz.views import home

urlpatterns= [
    path('register/', register, name='register-page'),
    path('', log_in, name='login-page'),
    path('logout/', log_out, name='logout-page'),
    path('home/', home, name='home-page')

]