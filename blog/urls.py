from django.urls import path
from .views import PostView,PostDetailsViewsp

urlpatterns = [
path('',PostView.as_view(),name='home'),
path('details/<int:pk>', PostDetailsViewsp.as_view(), name='postdetail_view'),
]

