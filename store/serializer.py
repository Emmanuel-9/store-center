from rest_framework import serializers
from .models import StorageUnits

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageUnits
        fields = ('slots','type_of_goods','start_date_of_storage')