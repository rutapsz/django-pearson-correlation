from django.urls import path
from .views import PearsonCorrelationView

urlpatterns = [
    path('pearson/', PearsonCorrelationView.as_view(), name='pearson-correlation'),
]
