from django.urls import path,include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('tasks',TaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
   # path('update/<int:pk>/',update_task),
    #path('delete/<int:pk>/',delete_task),
]