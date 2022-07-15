from django.urls import re_path
from api.views import ListView

urlpatterns = [
    re_path(r'^getLayawayList$', ListView.as_view())
]
