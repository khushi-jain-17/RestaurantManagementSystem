from rest_framework import serializers
from .models import MenuItem, Category 



class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name','description','price','category']

    def create(self, validated_data):
        return MenuItem.objects.create(**validated_data)
    

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'    