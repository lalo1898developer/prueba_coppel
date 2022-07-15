from django.urls import re_path
from api.views import CreateView

urlpatterns = [
    re_path(r'^users$', CreateView.as_view())
]
