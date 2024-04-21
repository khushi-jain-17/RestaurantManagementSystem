from django.urls import path
from . views import MenuCreateView, MenuListView, MenuDetailView, MenuUpdateView, MenusListView, MenuAPIView

app_name='menu'







urlpatterns = [
    path('menu-create/', MenuCreateView.as_view(), name='menu_create'),
    path('menu-list/', MenuListView.as_view(), name='menu_list'),
    path('menu-detail/<int:pk>/', MenuDetailView.as_view(), name='menu_detail'),
    path('menu-get-update-destroy/<int:pk>/', MenuUpdateView.as_view(), name='menu-update-destroy'),
    path('my-menu/list/', MenusListView.as_view(), name='my-menu'),
    path('menu-search/', MenuAPIView.as_view(), name='menu_search'),
]

