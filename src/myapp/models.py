from django.db import models
from django.contrib.auth.models import User


class RemindTime(models.Model):
	time = models.PositiveIntegerField()

	def __str__(self):
		return self.time.__str__()


class Event(models.Model):
	name = models.CharField(max_length=120)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField(blank=True, null=True)
	user_event = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.ForeignKey(RemindTime, on_delete=models.SET_NULL, null=True)
	discription = models.TextField()


	def save(self, *args, **kwargs):
		if self.end_time is None:
			self.end_time = self.start_time
			self.end_time = self.end_time.replace(hour=23, minute=59, second=59)
		super().save(*args, **kwargs)