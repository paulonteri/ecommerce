from rest_framework import serializers

from products.models import ItemVariation, Variation, Item, SubCategory, Brand


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['title']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title']


class ItemSerializer(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'sub_category',
            'brand',
            'description',
            'image'
        )

    def get_sub_category(self, obj):
        return SubCategorySerializer(obj.sub_category).data['title']

    def get_brand(self, obj):
        return BrandSerializer(obj.brand).data['title']


class ItemVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariation
        fields = (
            'id',
            'value',
            'attachment'
        )


class VariationDetailSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = Variation
        fields = (
            'id',
            'name',
            'item'
        )

    def get_item(self, obj):
        return ItemSerializer(obj.item).data


class VariationSerializer(serializers.ModelSerializer):
    item_variations = serializers.SerializerMethodField()

    class Meta:
        model = Variation
        fields = (
            'id',
            'name',
            'item_variations'
        )

    def get_item_variations(self, obj):
        return ItemVariationSerializer(obj.itemvariation_set.all(), many=True).data


class ItemVariationDetailSerializer(serializers.ModelSerializer):
    variation = serializers.SerializerMethodField()

    class Meta:
        model = ItemVariation
        fields = (
            'id',
            'value',
            'attachment',
            'variation'
        )

    def get_variation(self, obj):
        return VariationDetailSerializer(obj.variation).data


class ItemDetailSerializer(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'sub_category',
            'brand',
            'description',
            'image',
            'variations'
        )

    def get_sub_category(self, obj):
        return SubCategorySerializer(obj.sub_category).data['title']

    def get_brand(self, obj):
        return BrandSerializer(obj.brand).data['title']

    def get_variations(self, obj):
        return VariationSerializer(obj.variation_set.all(), many=True).data
