from rest_framework import serializers


from .models import *


class AttrKeySerializer(serializers.ModelSerializer):
    attr_key_id = serializers.ReadOnlyField()

    class Meta:
        model = AttrKey
        fields = ['attr_key_id', 'attr_name', 'cat_id']


class AttrValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttrValue
        fields = ['attr_value', 'attr_key_id']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['cat_id', 'parent_id', 'cat_name']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['bnd_id', 'bnd_name']


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.ReadOnlyField(source='brand_id.bnd_name')
    pdt_id = serializers.ReadOnlyField()

    class Meta:
        model = Product
        # TODO (murphy) brand_id 是可有可无的
        fields = ['pdt_id', 'pdt_name', 'pdt_desc', 'cat_id', 'brand_id', 'brand']
        extra_kwargs = {
            'brand_id': {'write_only': True}
        }


class ProductSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecs
        fields = ['pdt_spec_name', 'pdt_spec_price', 'pdt_id']


class ProductSpecsToAttrValSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecsToAttrVal
        fields = ['pdt_spec_id', 'attr_val_id']
