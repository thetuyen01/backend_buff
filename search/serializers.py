from rest_framework import serializers
from .models import Search

class SearchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'
