from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q


def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'

    address_query = request.GET.get('q')
    property_type = request.GET.get('property_type', None)
    if address_query and property_type:
        print(address_query)
        print(property_type)
        # 검색 기능을 사용하기 위해서 이름과 타입으로 비교(이름, rent or sale)
        property_list = property_list.filter(
            Q(name__icontains=address_query) &
            Q(property_type__icontains=property_type[0])
        ).distinct()
    else:
        context = {
            
        }

        return render(request, template, context)

    print(property_list)
    context = {
        'property_list': property_list
    }

    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'
    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReserveForm()
    context = {
        'property_detail': property_detail,
        'reserve_form': reserve_form,
    }

    return render(request, template, context)
