from django import views
from .views import AlimentacaoView, ImportFileAlimentacaoView
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alimentacao', AlimentacaoView)

urlpatterns = [
     path('alimentacao', AlimentacaoView.as_view(), name='list_alimentacao'),
     path('importAlimentacao', ImportFileAlimentacaoView.as_view())
]

