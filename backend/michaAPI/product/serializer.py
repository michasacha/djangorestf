from .models import Product
from rest_framework import serializers

class productSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
       model = Product
       fields = ('name','content', 'price', 'my_discount')

    def get_my_discount(self, obj):
        return obj.get_discount