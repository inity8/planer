from django.shortcuts import render
from django.http import HttpResponse
from myapp.serializer import EventSerializerGET, EventSerializerPOST
from rest_framework.generics import CreateAPIView, ListAPIView
from myapp.models import Event
from django.core.mail import send_mail


class EventCreateView(CreateAPIView):
	serializer_class = EventSerializerPOST


class EventListView(ListAPIView):
	serializer_class = EventSerializerGET
	queryset = Event.objects.all()
