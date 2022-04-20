from hashlib import new
from rest_framework import generics
from .models import Alimentacao
from .serializers import AlimentacaoSerializer, FileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
import re


class AlimentacaoView(generics.ListCreateAPIView):
    queryset = Alimentacao.objects.all()
    serializer_class = AlimentacaoSerializer

    def saveAll(self, data):
        responses = []
        for alimentacao in data:
            serializerAlimentacao = AlimentacaoSerializer(data=alimentacao)
            if serializerAlimentacao.is_valid():
                serializerAlimentacao.save()
                responses.append(serializerAlimentacao.data)
            else:
                responses.append(serializerAlimentacao.errors)
        return Response({"status": "info", "data": responses}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AlimentacaoSerializer(data=request.data)
        if type(request.data) is list:
            return self.saveAll(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ImportFileAlimentacaoView(APIView):
    permission_classes = []
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():

            data = request.FILES['file']
            alimentacoes = []
            for line in data:
                numbers = re.findall('[^\D]+', line.decode())
                alimentacao = {}
                if numbers:
                    alimentacao["name"] = re.search(
                        '\D+', line.decode()).group().strip()
                    alimentacao["quantity"] = int(numbers[0])
                    alimentacao["proteins"] = int(numbers[1])
                    alimentacao["carbohydrates"] = int(numbers[2])
                    alimentacao["fat"] = int(numbers[3])
                    alimentacoes.append(alimentacao)

            response = AlimentacaoView.saveAll(self, alimentacoes)
            return response
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
