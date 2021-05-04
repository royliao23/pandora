from rest_framework import viewsets


from .models import *
from .serializers import *
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import SearchFilter, OrderingFilter

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company_Staff.objects.all()
    serializer_class = CompanySerializer
    #filter_backends = (filters.SearchFilter,)
    
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields =('company',)
    #ordering =('index',)
    #search_fields = ("company")
class FoodViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = FoodSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields =('name',)
    #ordering =('name',)
    #search_fields = ('favoriteFoods')