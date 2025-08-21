from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Univeristy,Program
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Univeristy
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model=Program
        fields = '__all__'