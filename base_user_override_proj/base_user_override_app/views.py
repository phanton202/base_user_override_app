# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignupSerializer
from rest_framework.permissions import IsAuthenticated

class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dashboard(APIView):
    permission_classes =[IsAuthenticated]

    def get(self, request):
        username= request.user.email
        return Response({"username":username})
