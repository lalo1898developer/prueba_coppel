from django.urls import re_path
from api.views import AddView

urlpatterns = [
    re_path(r'^addToLayaway$', AddView.as_view())
]
