from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from django.shortcuts import render

from .models import Reward

class IndexView(generic.ListView):
    template_name = 'rewards/index.html'
    context_object_name = 'rewards_list'
    
    def get_queryset(self):
        return Reward.objects

# Create your views here.
