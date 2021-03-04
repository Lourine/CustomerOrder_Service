from django.urls import path
from.views import RegisterView, LoginAPIView, VerifyEmail

urlpatterns=[
    path('register/',RegisterView.as_view(),name="register"),
    path('Login/', LoginAPIView.as_view(),name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
]