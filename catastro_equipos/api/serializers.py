from rest_framework import serializers
from catastro_equipos.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    def validate_product_quantity(value):
        if value >= 1:
            return value
        else:  
            raise serializers.ValidationError('La cantidad debe ser mayor o igual a 1')

    def validate_product_data(value):
        if len(value) > 3:
            return value
        else:
            raise serializers.ValidationError('Por favor, Ingrese descripcion valida')

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True, default=0)
#     product_name = serializers.CharField(validators=[validate_product_data])
#     type_product = serializers.CharField()
#     model_product = serializers.CharField()
#     mac_address = serializers.CharField()
#     serie_coment = serializers.CharField()
#     active_code = serializers.CharField()
#     product_stattus = serializers.CharField()
#     product_quantity = serializers.IntegerField(validators=[validate_product_quantity])
    
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
    
    
#     def update(self, instance, validated_data):
#         instance.product_name = validated_data.get('product_name', instance.product_name)
#         instance.type_product = validated_data.get('type_product', instance.type_product)
#         instance.model_product = validated_data.get('model_product', instance.model_product)
#         instance.mac_address = validated_data.get('mac_address', instance.mac_address)
#         instance.serie_coment = validated_data.get('serie_coment', instance.serie_coment)
#         instance.active_code = validated_data.get('active_code', instance.active_code)
#         instance.product_stattus = validated_data.get('product_stattus', instance.product_stattus)
#         instance.product_quantity = validated_data.get('product_quantity', instance.product_quantity)
#         instance.save()
#         return instance
        
    
    