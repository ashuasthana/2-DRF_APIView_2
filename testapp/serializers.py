from rest_framework import serializers

#create serialzer class
class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)