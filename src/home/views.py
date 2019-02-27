from django.shortcuts import render
from property.models import Property, Category
from agents.models import Agent


def home(request):
    category_list = Category.objects.all()
    property_list = Property.objects.all()
    agent_list = Agent.objects.all()
    template = 'home/home.html'
    context = {
        'category_list_home': category_list,
        'property_list_home': property_list,
        'agent_list_home': agent_list,
    }
    return render(request, template, context)
