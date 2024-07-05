from rest_framework import serializers

from .models import Header, HeaderBody, Tariffs

class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class HeaderBodySerializers(serializers.ModelSerializer):
    class Meta:
        model = HeaderBody
        fields = '__all__'


class TariffsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tariffs
        fields = '__all__'