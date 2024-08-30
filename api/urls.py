from django.urls import path
from .views import SendOTP,VerifyAndAuthenticateUser

urlpatterns = [
    path('send-otp/', SendOTP.as_view(), name='send_otp'),
    path('verify-otp/', VerifyAndAuthenticateUser.as_view(), name='verify_otp'),
    #path('authenticate/', AuthenticateUser.as_view(), name='authenticate_user'),
]
