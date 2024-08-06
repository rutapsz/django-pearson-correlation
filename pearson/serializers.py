from rest_framework import serializers

class DataSetSerializer(serializers.Serializer):
    data1 = serializers.ListField(child=serializers.FloatField(), required=False)
    data2 = serializers.ListField(child=serializers.FloatField(), required=False)
    file = serializers.FileField(required=False)