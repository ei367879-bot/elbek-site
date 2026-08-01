import django_filters
from products.models import Product, ProductImage
class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    class Meta:
        model = Product
        fields = ['category', "price_min", "price_max", 'price']
urls.py
    # Product
    path('products/', ProductListApiView.as_view(), name='products'),
    path('products/create/', ProductCreateApiView.as_view(), name='products-create'),
    path('products/<int:pk>', ProductDetailApiView.as_view(), name='products-detail'),

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Product
class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', "category__name"]
    pagination_class = ProductPagination
class ProductCreateApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAdminUser]
class ProductDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAdminUser]
class ProductImageFilter(django_filters.FilterSet):
    class Meta:
        model = ProductImage
        fields = ['product']

