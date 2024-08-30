from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
import random
import jwt
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.conf import settings
from twilio.rest import Client

class SendOTP(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"error": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)
        if len(phone_number) != 13:
            return Response({"error": "Phone number should have country code and 10 digits."}, status=status.HTTP_400_BAD_REQUEST)
        otp = str(random.randint(1000, 9999))

        user, created = User.objects.get_or_create(phone_number=phone_number)
        user.otp = otp
        user.is_verified = False
        user.save()

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        try:
            message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
            )
        except TwilioRestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)



  

class VerifyAndAuthenticateUser(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')

        if not phone_number or not otp:
            return Response({"error": "Phone number and OTP are required."}, status=status.HTTP_400_BAD_REQUEST)

        if len(phone_number) != 13:
            return Response({"error": "Phone number should have country code and 10 digits."}, status=status.HTTP_400_BAD_REQUEST)

        if len(otp) != 4:
             return Response({"error": "OTP should've 4 digits."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number, otp=otp)
        except User.DoesNotExist:
            return Response({"error": "Invalid Credentials."}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_verified:
            user.is_verified = True
            user.save()

            payload = {
            'id': user.id,
            'phone_number': user.phone_number
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return Response({"message": "OTP verified successfully.", "token": token}, status=status.HTTP_200_OK)

        return









