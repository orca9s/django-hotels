from django.db.models import Count
from django.shortcuts import render


from agents.models import Agent
from property.models import Category, Property


def home(request):
    category_list = Category.objects.annotate(property_count=Count('property')).values(
        # 카테고리 모델에서 count를 가지고 있지 않아 템플릿에 총 갯수를 뿌려줄 수 없기 때문에 아래 인자를 포함해서
        # 카운트를 추가해서 category_list_home을 만들어줌
        # id 인자는 도시별로 보여주는 view를 작성하기 위해 나중에 추가함
        # property_location_total_detail
        'id',
        'category_name',
        'property_count',
        'image',
    )
    property_list = Property.objects.all()
    agent_list = Agent.objects.all()
    template = 'home/home.html'
    context = {
        'category_list_home': category_list,
        'property_list_home': property_list,
        'agent_list_home': agent_list,
    }
    return render(request, template, context)
