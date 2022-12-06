from django.urls import path
from .views import home, log_in,register, log_out, test

urlpatterns= [
    path('home/', home, name='home-page'),
    path('register/', register, name='register-page'),
    path('login/', log_in, name='login-page'),
    path('logout/', log_out, name='logout-page'),
    path('test/', test, name='test-page')
]