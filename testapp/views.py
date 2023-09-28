from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NameSerializer

# Create your views here.
class TestAPIVIEW(APIView):
    def get(self,request,*awrgs,**kwargs):
        colors=['red','yrllow','green','white','blue']
        return Response({'msg':"Happy Holi",'colors':colors})
    
    def post(self,request,*awrgs,**kwargs):
        # data=request.data
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            name=serializer.data.get('name')
            msg=f"Hello {name}, Happy Diwali"
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
        
    def put(self,request,*awrgs,**kwargs):
            return Response({'msg':"This is from 'put' method."})   
    def patch(self,request,*awrgs,**kwargs):
            return Response({'msg':"This is from 'patch' method."})  
    def delete(self,request,*awrgs,**kwargs):
            return Response({'msg':"This is from 'delete' method."})   
        
