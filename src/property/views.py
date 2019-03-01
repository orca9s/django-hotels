from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q


def property_list(requset):
    property_list = Property.objects.all()
    template = 'property/list.html'
    context = {
        'property_list': property_list,
    }
    return render(requset, template, context)


def property_search_list(request):
    property_search_list = Property.objects.all()
    template = 'property/search_list.html'

    address_query = request.GET.get('q')
    property_type = request.GET.get('property_type', None)
    if address_query and property_type:
        print(address_query)
        print(property_type)
        # 검색 기능을 사용하기 위해서 이름과 타입으로 비교(이름, rent or sale)
        property_search_list = property_search_list.filter(
            Q(name__icontains=address_query) &
            Q(property_type__icontains=property_type[0])
        ).distinct()
    else:
        return render(request, template)

    context = {
        'property_search_list': property_search_list
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


# 메인페이지 에서 지역별 현황을 눌렀을 경우 지역상품을 보여주는 페이지
def property_location_total_detail(request, location_id):
    """
    1. 템플릿이 로드 되면서 내가 선택할 부분의 url을 받아옴
    2. url을 통해 내가 선택한 지역의 ID값을 가지고(url에 담아서 보냄)
    3. category(지역)모델에 접근하여 url에 담아온 ID값과 일치하는 지역을 찾은 후
    4. Property모델로 이동하여 category에서 받아온 ID와(지역) Property(호텔)과 연결된 지역 ID값 비교
    4. filter를 통해서 내가 선택한 지역의 ID값을 가지고 있는 property들을 모두 찾는다
    5. 찾은 값을 context에 담아서 total_detail.html로 리턴시킨다.
    :param request:
    :param location_id:
    :return:
    """
    # 카테고리(지역)의 id를 받아옴
    property_location = Category.objects.get(id=location_id)
    # property(호텔)에 입력된 지역과 위에서 받아온 category(지역) id값을 비교해서 필터링
    property_location_total_detail = Property.objects.filter(category__id=property_location.id)
    template = 'property/total_detail.html'
    context = {
        'property_location_total_detail': property_location_total_detail,
    }
    return render(request, template, context)
