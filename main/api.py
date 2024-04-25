from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import  JobSerializer
from rest_framework.response import Response
from .models import Main
from rest_framework import generics

@api_view(['GET', 'POST'])
def main_list_api(request):
    all_mains = Main.objects.all() 
    data =JobSerializer(all_mains, many=True).data
    return Response({'data':data})
    
@api_view(['GET'])
def main_detail_api(request , id):
    main_detail=Main.objects.get(id=id)
    data =JobSerializer(main_detail).data
    return Response({'data':data})
    
class JobListApi(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = JobSerializer
    
    
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Main.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
    
    