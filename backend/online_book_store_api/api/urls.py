from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('book-list/', views.showAll, name='book-list'),
    path('book-detail/<int:id>/', views.viewBook, name='book-detail'),
    path('book-create/', views.addBook, name='book-create'),
    path('test/', views.sp_get, name='test'),
    
]