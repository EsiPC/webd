from django.urls import path
from .views import Messageview

urlpatterns=[
    path('',Messageview.as_view(),name='message'),
]