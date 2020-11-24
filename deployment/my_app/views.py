from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':

        try:
            image = request.FILES['scene']
            print("image.name")
            folder = 'media/images/'
            filename = str(image.name)

            media_path = folder+filename
            print(media_path)

            prediction = '2'

            print("worked")
            data = {"image_path": media_path, "prediction": prediction}

            return render(request, 'results.html', {'data': data})

        except Exception as e:
            print('The Error is',e)

    return HttpResponse("Failed")



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


