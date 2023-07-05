from django.shortcuts import render
from .models import ScreenShot, User
from .serializer import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ScreenShotView(ViewSet):
    def create(self,request):
        serializer_data=ScreenShotSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            user_obj,created= User.objects.get_or_create(IP=serializer_data.data['IP'])
            return Response(serializer_data.data,status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk):
        try:
            user_obj=User.objects.get(username=pk)
            ss_obj=ScreenShot.objects.filter(IP=user_obj.IP)[::-1]
            if len(ss_obj)==0:
                return Response({'msg':'Not Found !!!'}, status=status.HTTP_404_NOT_FOUND)
            serializer_data=ScreenShotSerializer(ss_obj,many=True)
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        except:
            return Response({'msg':'Not Found !!!'}, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self,request,pk):
        try:
            if ScreenShot.objects.filter(id=pk).exists():
                ss_obj=ScreenShot.objects.get(id=pk)
                ss_obj.delete()
                return Response({'msg':'ScreenShot Deleted!!'},status=status.HTTP_202_ACCEPTED )
            user_obj=User.objects.get(username=pk)
            ss_obj=ScreenShot.objects.filter(IP=user_obj.IP)
            ss_obj.delete()
            return Response({'msg':'ScreenShots Deleted!!'},status=status.HTTP_202_ACCEPTED )
        except:
            return Response({'msg':'Not Found !!!'}, status=status.HTTP_404_NOT_FOUND)
            

        
        
    
    