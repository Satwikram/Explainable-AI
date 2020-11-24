from PIL.Image import Image
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')

def predict(request):

    if request.method == 'POST':

        image = request.FILES['scene']
        folder = 'media/images/'
        print("The Type is:",type(image))
        fileName, fileExtension = os.path.splitext(image.name)
        print(fileName)
        extension = ['.png', '.jpg']
        print(extension)

        if fileExtension not in extension:
            print("Am in If",fileExtension)
            messages.info(request, "The patient condition is: Pneumonia")
            return redirect("predict")

        filename = str(image.name)

        media_path = folder+filename
        print(media_path)

        prediction = 2

        print("worked")
        data = {"image_path": media_path, "prediction": prediction}

        return render(request, 'results.html', {'data': data})

    return render(request, "home.html")

class PredictAPIView(APIView):

    # Post Method
    def post(self, request):

        #img = request.FILES['scene']
        #img1 = request.data
        #path = 'media/'+str(img.name)
        #data = {'image_path': path, 'prediction': 2}

        serializer = PredictSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            print("The Serializer is:",serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Else, return 400 Bad Request
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


