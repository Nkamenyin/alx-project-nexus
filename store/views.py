from rest_framework import generics, filters

from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# -------------------------------
# Pagination
# -------------------------------
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# -------------------------------
# CATEGORY VIEWS
# -------------------------------
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="List all categories",
        operation_description="Retrieve all categories.",
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Create a new category",
        operation_description="Admin only. Provide name, slug, and optional description.",
        request_body=CategorySerializer,
        responses={201: CategorySerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Retrieve a category",
        operation_description="Get a category by ID.",
        responses={200: CategorySerializer, 404: "Not found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Update a category",
        operation_description="Admin only. Update a category by ID.",
        request_body=CategorySerializer,
        responses={200: CategorySerializer, 404: "Not found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Delete a category",
        operation_description="Admin only. Delete a category by ID.",
        responses={204: "No content", 404: "Not found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# -------------------------------
# PRODUCT VIEWS
# -------------------------------
@method_decorator(cache_page(60*15), name='dispatch')  # cache for 15 minutes
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True, stock__gt=0)
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'description']
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="List all products",
        operation_description=(
            "Retrieve all active products.\n\n"
            "Supports search: ?search=keyword\n"
            "Supports ordering: ?ordering=price or ?ordering=created_at"
        ),
        responses={200: ProductSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Create a new product",
        operation_description="Admin only. Provide name, category, price, stock, and optional image.",
        request_body=ProductSerializer,
        responses={201: ProductSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Retrieve a product",
        operation_description="Get a product by ID.",
        responses={200: ProductSerializer, 404: "Not found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Update a product",
        operation_description="Admin only. Update a product by ID.",
        request_body=ProductSerializer,
        responses={200: ProductSerializer, 404: "Not found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Delete a product",
        operation_description="Admin only. Delete a product by ID.",
        responses={204: "No content", 404: "Not found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
