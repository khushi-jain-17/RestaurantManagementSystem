from django.urls import path
from . views import MenuCreateView, MenuListView, MenuDetailView, MenuUpdateView, MenusListView, CategoryAPIView, ItemsAPIView

app_name='menu'







urlpatterns = [
    path('menu-create/', MenuCreateView.as_view(), name='menu_create'),
    path('menu-list/', MenuListView.as_view(), name='menu_list'),
    path('menu-detail/<int:pk>/', MenuDetailView.as_view(), name='menu_detail'),
    path('menu-get-update-destroy/<int:pk>/', MenuUpdateView.as_view(), name='menu-update-destroy'),
    path('my-menu/list/', MenusListView.as_view(), name='my-menu'),
    path('category-search/', CategoryAPIView.as_view(), name='category_search'),
    path('menu_item/search/',ItemsAPIView.as_view(),name='menu_item_search')
]

