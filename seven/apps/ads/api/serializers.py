from rest_framework import serializers

from ..models import Country, Category, Ad


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name

    class Meta:
        model = Ad
        fields = (
            'id',
            'title',
            'description',
            'country',
            'category',
            'msg_allow',
            'pic1',
            'pic2',
            'pic3',
            'pic4',
            'pic5',
            'category_name'
        )

