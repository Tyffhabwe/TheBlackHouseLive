"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.HomepageView.as_view(), name='home_page'),
    path('whatwedo/', views.WhatWeDoView.as_view(), name='what_we_do'),
    path('meettheteam', views.MeetTeamView.as_view(), name='meet_the_team'),
    path('episodes/', views.PodcastEpisodeView.as_view(), name='podcast_episodes'),
    path('homepage/edit/<int:pk>', views.UpdateHomePageView.as_view(), name='update_homepage'),
    path('whatwedo/edit/<int:pk>', views.UpdateWhatWeDoPageView.as_view(), name='update_whatwedo'),
    path('meettheteam/edit/<int:pk>', views.UpdateMeetTeamView.as_view(), name='update_meettheteam'),
    path('episodes/edit/<int:pk>', views.UpdatePodcastEpisodeView.as_view(), name='update_podcast_episode'),
    path('episodes/create', views.CreatePodcastEpisodeView.as_view(), name='create_podcast_episode'),
    path('episodes/delete/<int:pk>', views.DeletePodcastEpisodeView.as_view(), name='delete_podcast_episode'),
    path('calender/', views.calender, name='calender'),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
