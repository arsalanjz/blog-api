from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer,UserProfileSerializer



class UserRegisterView(APIView):

    def post(self, request, *args, **kwargs):
        ser_data = UserRegisterSerializer(data=request.data)

        if ser_data.is_valid():
            ser_data.save()
            return Response({"message": "Ceated Account Successful"}, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
