from myapp.models import Event, RemindTime
from rest_framework.serializers import ModelSerializer


class RemindTimeSerializer(ModelSerializer):
	class Meta:
		model = RemindTime
		fields = "__all__"


class EventSerializerGET(ModelSerializer):
	time = RemindTimeSerializer()
	class Meta:
		model = Event
		fields = "__all__"


class EventSerializerPOST(ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"