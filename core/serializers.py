from rest_framework import serializers
from .models import Alimentacao, File

class AlimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacao
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
