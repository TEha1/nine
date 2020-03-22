# Rest
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
# Models
from ..models import Country, Category, Ad
# Serializers
from .serializers import CategorySerializer, CountrySerializer, AdSerializer



class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


#
class AdsCreateListView(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (AllowAny,)


class AdsSearchListView(ListAPIView):
    serializer_class = AdSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Ad.objects.filter(title__icontains=self.kwargs['title'])


class AdsRUView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (AllowAny,)


class CountryRUView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


class CategoryRUView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
