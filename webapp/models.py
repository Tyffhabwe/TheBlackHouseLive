from django.db import models
from datetime import datetime


class WhatWeDo(models.Model):
	"""Class to store the data for the what we do page. Ideally this will have 
	only one row, cause thats all we need. Stored in database to make it editable 
	cause thats what I'm looking for."""
	title = models.CharField(max_length=200)
	right_paragraph = models.TextField()
	left_paragraph = models.TextField()

	def __str__(self):
		return self.title


class PodcastEpisode(models.Model):
	"""Class to store data for the On Air page. Video links mostly"""
	video_link = models.TextField(null=True)
	video_title = models.CharField(max_length=200, null=True)
	video_text = models.TextField(null=True)
	upload_date = models.DateTimeField(null=True, default=datetime.now)

	def __str__(self):
		return self.video_title

class Home(models.Model):
	"""Class to store data for the Home page. Only need one instance"""
	title = models.CharField(max_length=200, null=True)
	top_text = models.TextField(null=True)
	iframe_link = models.CharField(null=True, max_length=500)

	def __str__(self):
		return self.title

class MeetTeam(models.Model):
	"""Class to store data for the Meet Team page. Need 3 instances """
	#Add a way to store photos here
	member_name = models.CharField(max_length=200, null=True)
	photo = models.ImageField(upload_to ='images/', null=True)
	writeup = models.TextField(null=True)

	def __str__(self):
		return self.member_name


"""Only one more needed for calender here once I figure out how to do that exactly"""
