from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.core.mail import send_mail
from sendmail import settings

class SendEmailAPIView(APIView):
    def post(self, request):
        subject = request.data.get('subject', None)
        message = request.data.get('message', None)
        name = request.data.get('name', None)
        to = request.data.get('to', None)
        
        if subject is None or message is None or to is None or name is None:
            return Response({"error": "Please provide all required fields"}, status=400)
        
        if len(subject) <= 0 or len(message) <= 0 or len(to) <= 0 or len(name) <= 0:
            return Response({"error": "Please provide all required fields"}, status=400)
        
        text = f''' ถึงคุณ {name}\n
        {message} \n'''
        sendmail = send_mail(
            subject,
            text,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False,
        )
        
        if sendmail == 1:
            return Response({"message": "Email sent successfully"}, status=200)
        
        return Response({"error": "Email not sent"}, status=400)        
