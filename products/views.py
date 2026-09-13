from django.shortcuts import render 
from rest_framework.viewsets import ModelViewSet 
from .models import Category, Product 
from .serializers import CategorySerializer, ProductSerializer
from .permissions import GetForUser

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    permission_classes = [GetForUser]

class ProductViewSet(ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

