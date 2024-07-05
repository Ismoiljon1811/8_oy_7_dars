from django.shortcuts import render

from .serializers import HeaderSerializers, HeaderBodySerializers, TariffsSerializers
from .models import Header, HeaderBody, Tariffs

from rest_framework.viewsets import ModelViewSet

class HeaderView(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers


class HeaderBodyView(ModelViewSet):
    lis = []
    all = HeaderBody.objects.all()
    for i in all:
        lis.append(i.id)
    lis = max(lis)
    for dele in all:
        if dele.id != lis:
            dele.delete()
    queryset = HeaderBody.objects.filter(id = lis)
    serializer_class = HeaderBodySerializers
 

class TariffsView(ModelViewSet):
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializers
