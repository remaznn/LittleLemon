
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework import generics , viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = bookingSerializer
   permission_classes = [IsAuthenticated] 

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer 

# class menuview(APIView):
#     def post(self,request):
#         serializer = menuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success" , "data":serializer.data})