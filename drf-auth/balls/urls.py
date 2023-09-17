from django.urls import path
from .views import BallListCreate, BallDetail

urlpatterns = [
    path('', BallListCreate.as_view()),
    path('<int:pk>/', BallDetail.as_view()),
]
