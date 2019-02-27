from django.shortcuts import render
from .models import Agent


def agents_list(request):
    agents_list = Agent.objects.all()
    template = 'agents/agents.html'
    context = {
        'agents_list': agents_list,
    }

    return render(request, template, context)