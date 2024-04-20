from django.urls import path
from . views import CreateView, MenuListView, MenuDetailView, MenuUpdateView

app_name='menu'







urlpatterns = [
    path('menu-create/', CreateView.as_view(), name='menu_create'),
    path('menu-list/', MenuListView.as_view(), name='menu_list'),
    path('menu-detail/<int:pk>/', MenuDetailView.as_view(), name='menu_detail'),
    path('menu-get-update-destroy/<int:pk>/', MenuUpdateView.as_view(), name='menu-update-destroy'),
]