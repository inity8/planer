from django.urls import path
from myapp.views import EventListView, EventCreateView

urlpatterns = [
	path("v1/list/", EventListView.as_view()),
	path("v1/create/", EventCreateView.as_view()),
]