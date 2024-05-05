from django.urls import path
from . import views

urlpatterns = [
    path('check/<str:pk>/', views.hello, name='check'),
    path('', views.create_view, name='home'),        
    path('view/', views.list_view, name='view'),        
    path('single/<int:pk>/', views.single_view, name='single'),        
    path('edit/<int:pk>', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:pk>', views.deleteView, name='delete')  
]
