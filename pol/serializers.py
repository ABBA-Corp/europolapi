from dataclasses import fields
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = About
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = "__all__"

