from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import  JobSerializer
from rest_framework.response import Response
from .models import Cleaning
from rest_framework import generics

@api_view(['GET', 'POST'])
def cleaning_list_api(request):
    all_cleanings = Cleaning.objects.all() 
    data =JobSerializer(all_cleanings, many=True).data
    return Response({'data':data})
    
@api_view(['GET'])
def cleaning_detail_api(request , id):
    cleaning_detail=Cleaning.objects.get(id=id)
    data =JobSerializer(cleaning_detail).data
    return Response({'data':data})
    
class JobListApi(generics.ListAPIView):
    queryset = Cleaning.objects.all()
    serializer_class = JobSerializer
    
    
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cleaning.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
    
    