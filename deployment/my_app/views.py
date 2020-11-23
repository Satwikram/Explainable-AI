from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

class PredictAPIView(APIView):

    # Post Method
    def post(self, request):
        serializer = PredictSerializer(data = request.data)
        print(serializer)

