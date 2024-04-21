from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import MenuItem, Category
from django.utils.decorators import method_decorator
from rest_framework import generics, status, views, filters 
from rest_framework.response import Response 
from django.http import HttpResponsePermanentRedirect
from .serializers import CreateSerializer, MenuItemSerializer
from authentication.decorators import *
from .pagination import CustomPagination



@method_decorator(has_role('myadmin'), name='dispatch')
class MenuCreateView(generics.CreateAPIView):
    serializer_class = CreateSerializer
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='insert token', type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config], operation_description="Create a Menu Item")
    def post(self,request):
        mi = request.data
        serializer = self.serializer_class(data=mi)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        menu_data = serializer.data
        return Response(menu_data, status=status.HTTP_201_CREATED)


@method_decorator(has_role('myadmin'), name='dispatch')
class MenuListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()  
    serializer_class = MenuItemSerializer  
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='write token', type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config],operation_description="Retrieve all menu items")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




@method_decorator(has_role('myadmin'), name='dispatch')
class MenuDetailView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer   

    @swagger_auto_schema(
        operation_description="Retrieve a menu item by ID",
        manual_parameters=[
            openapi.Parameter(
                name='token',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Token for authentication',
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        menu_item_id = kwargs.get('pk')
        menu_item = get_object_or_404(self.get_queryset(), pk=menu_item_id)
        serializer = self.get_serializer(menu_item)
        return Response(serializer.data)



@method_decorator(has_role('myadmin'), name='dispatch')
class MenuUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    @swagger_auto_schema(
        operation_description="Fetch a menu item by ID",
        manual_parameters=[
            openapi.Parameter(
                name='token',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Token for authentication',
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a menu item by ID",
        manual_parameters=[
            openapi.Parameter(
                name='token',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Token for authentication',
            )
        ]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a menu item by ID",
        manual_parameters=[
            openapi.Parameter(
                name='token',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Token for authentication',
            )
        ]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




@method_decorator(has_role('myuser'), name='dispatch')
class MenusListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()  
    serializer_class = MenuItemSerializer  
    pagination_class = CustomPagination
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='write token', type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config],operation_description="Retrieve all menu items")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




@method_decorator(has_role('myuser'), name='dispatch')
class MenuAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()  
    serializer_class = MenuItemSerializer  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'token',
            in_=openapi.IN_QUERY,
            description='write token',
            type=openapi.TYPE_STRING
        )
    ], operation_description="Search Menu Items")
    def get(self, request, *args, **kwargs):
        category_name = self.request.query_params.get('category', '')  
        queryset = MenuItem.objects.all()
        if category_name:
            queryset = queryset.filter(category__name__icontains=category_name)
        return self.list(request, *args, **kwargs)



#     search_fields = ['category']
#     filter_backends  = (filters.SearchFilter,)
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
