from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import  JobSerializer
from rest_framework.response import Response
from .models import Moving
from rest_framework import generics

@api_view(['GET', 'POST'])
def moving_list_api(request):
    all_movings = Moving.objects.all() 
    data =JobSerializer(all_movings, many=True).data
    return Response({'data':data})
    
@api_view(['GET'])
def moving_detail_api(request , id):
    moving_detail=Moving.objects.get(id=id)
    data =JobSerializer(moving_detail).data
    return Response({'data':data})
    
class JobListApi(generics.ListAPIView):
    queryset = Moving.objects.all()
    serializer_class = JobSerializer
    
    
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moving.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
    
    