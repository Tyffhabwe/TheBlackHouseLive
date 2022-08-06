from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template import loader
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

from .models import *

# Create your views here.

class HomepageView(generic.ListView):
	template_name = 'webapp/homepage.html'
	context_object_name = 'page_content'

	def get_queryset(self):
		"""Return singular object of pk=1 for home, and most recent podcast episode"""
		queryset = {
			'home': Home.objects.get(pk=1),
			'latest_episode': PodcastEpisode.objects.last()
		}
		return queryset


class WhatWeDoView(generic.ListView):
	template_name = 'webapp/what_we_do.html'
	context_object_name = 'page_content'

	def get_queryset(self):
		"""Return singular object of pk=1"""
		return WhatWeDo.objects.get(pk=1)


class MeetTeamView(generic.ListView):
	template_name = 'webapp/meet_the_team.html'
	context_object_name = 'members'

	def get_queryset(self):
		"""Return singular object of pk=1"""
		return MeetTeam.objects.all()


class PodcastEpisodeView(generic.ListView):
	template_name = 'webapp/podcast_episodes.html'
	context_object_name = 'episodes'

	def get_queryset(self):
		"""Return all the episodes in the database"""
		return PodcastEpisode.objects.all().order_by('-upload_date')

class CreatePodcastEpisodeView(LoginRequiredMixin, generic.CreateView):
	model = PodcastEpisode
	template_name = 'webapp/update_podcast_episodes.html'
	fields = ['video_link', 'video_title', 'video_text', 'upload_date']
	success_url = reverse_lazy('home_page')


class DeletePodcastEpisodeView(LoginRequiredMixin, generic.DeleteView):
	model = PodcastEpisode
	template_name = 'webapp/delete_podcast_episode.html'
	success_url = reverse_lazy('home_page')


class UpdateHomePageView(LoginRequiredMixin, generic.UpdateView):
	"""Allows admins to change the content of the homepage"""
	model = Home
	template_name = 'webapp/update_homepage.html'
	fields = ['title', 'top_text', 'iframe_link']
	success_url = reverse_lazy('home_page')

class UpdateWhatWeDoPageView(LoginRequiredMixin, generic.UpdateView):
	"""Allows admin to change content of the what we do page"""
	model = WhatWeDo
	template_name = 'webapp/update_whatwedopage.html'
	fields = ['title', 'right_paragraph', 'left_paragraph']
	success_url = reverse_lazy('what_we_do')


class UpdateMeetTeamView(LoginRequiredMixin, generic.UpdateView):
	"""Allows admin to change what is on the meet the team page. Always 
	be exactly 3 team members on that page. Can Upload images if need be.
	"""
	model = MeetTeam
	template_name = 'webapp/update_meetteam.html'
	fields = ['member_name', 'photo', 'writeup']
	success_url = reverse_lazy('meet_the_team')


class UpdatePodcastEpisodeView(LoginRequiredMixin, generic.UpdateView):
	"""Allows admin to change content of each episode upload"""
	model = PodcastEpisode
	template_name = 'webapp/update_podcast_episodes.html'
	fields = ['video_link', 'video_title', 'video_text', 'upload_date']
	success_url = reverse_lazy('podcast_episodes')

def calender(request):
	""" Returns a page with a google calender so people can see what will happen in future"""
	return render(request, 'webapp/calender.html')
