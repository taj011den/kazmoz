from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import  DemolishSerializer
from rest_framework.response import Response
from .models import Demolish
from rest_framework import generics

@api_view(['GET', 'POST'])
def demolish_list_api(request):
    all_demolishs = Demolish.objects.all() 
    data =DemolishSerializer(all_demolishs, many=True).data
    return Response({'data':data})
    
@api_view(['GET'])
def demolish_detail_api(request , id):
    demolish_detail=Demolish.objects.get(id=id)
    data =DemolishSerializer(demolish_detail).data
    return Response({'data':data})
    
class JobListApi(generics.ListAPIView):
    queryset = Demolish.objects.all()
    serializer_class = DemolishSerializer
    
    
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Demolish.objects.all()
    serializer_class = DemolishSerializer
    lookup_field = 'id'
    
    