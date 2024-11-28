from django.shortcuts import render,  get_object_or_404
def main_page(request):
    return render(request, 'main/main.html')


from django.db.models import Count
from .models import MicroVsPlants, CompVsMicro

from django.core.paginator import Paginator

def plant_page(request):
    # Get filter parameters from the request
    common_name = request.GET.get('common_name', '').strip()
    scientific_name = request.GET.get('scientific_name', '').strip()
    microorganism_name = request.GET.get('microorganism_name', '').strip()

    # Start with the full queryset
    data = MicroVsPlants.objects.values(
        'plant__id',
        'plant__common_name',
        'plant__scientific_name',
        'micro__id',
        'micro__name'
    )

    # Apply filters if values are provided
    if common_name:
        data = data.filter(plant__common_name__icontains=common_name)
    if scientific_name:
        data = data.filter(plant__scientific_name__icontains=scientific_name)
    if microorganism_name:
        data = data.filter(micro__name__icontains=microorganism_name)

    # Annotate with the count of records for each plant/microorganism combination
    data = data.annotate(record_count=Count('id'))

    # Pagination: Show 200 items by default, with an option to load more
    page_number = request.GET.get('page', 1)
    paginator = Paginator(data, 200)  # 200 items per page
    page_obj = paginator.get_page(page_number)

    context = {
        'data': page_obj,
        'common_name': common_name,
        'scientific_name': scientific_name,
        'microorganism_name': microorganism_name
    }

    return render(request, 'main/plant.html', context)



def plant_view_page(request, plant_id, micro_id):
    tests = MicroVsPlants.objects.filter(plant_id=plant_id, micro_id=micro_id)
    context = {'tests': tests}
    return render(request, 'main/plant_view.html', context)


def detail_view(request, test_id):
    test_detail = get_object_or_404(MicroVsPlants, pk=test_id)
    return render(request, 'main/plant_view_info.html', {'detail': test_detail})


from django.core.paginator import Paginator

def compounds_page(request):
    # Get filter parameters
    compound_name = request.GET.get('compound_name', '').strip()
    micro_name = request.GET.get('micro_name', '').strip()

    # Annotate data with record count
    data = CompVsMicro.objects.select_related('compound', 'micro').values(
        'compound__id',
        'compound__name',
        'micro__id',
        'micro__name'
    ).annotate(record_count=Count('id'))

    # Apply filters
    if compound_name:
        data = data.filter(compound__name__icontains=compound_name)
    if micro_name:
        data = data.filter(micro__name__icontains=micro_name)

    # Pagination: Show 200 items by default, with an option to load more
    page_number = request.GET.get('page', 1)
    paginator = Paginator(data, 200)  # 200 items per page
    page_obj = paginator.get_page(page_number)

    context = {
        'data': page_obj,
        'compound_name': compound_name,
        'micro_name': micro_name
    }
    return render(request, 'main/compounds.html', context)


# View for displaying detailed records
def compound_records(request, compound_id, micro_id):
    records = CompVsMicro.objects.filter(compound__id=compound_id, micro__id=micro_id)
    context = {'records': records}
    return render(request, 'main/compound_records.html', context)

def record_detail(request, record_id):
    record = get_object_or_404(CompVsMicro, id=record_id)
    return render(request, 'main/record_detail.html', {'record': record})


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import ExtractsMicroImpact

def extracts_page(request):
    # Get filter parameters
    extract_name = request.GET.get('extract_name', '').strip()
    micro_name = request.GET.get('micro_name', '').strip()

    # Start with the full queryset and select related fields
    data = ExtractsMicroImpact.objects.select_related('extract', 'micro').values(
        'extract__name',
        'micro__name',
        'num_of_experiments',
        'num_of_impacts',
        'avg_impact'
    )

    # Apply filters if values are provided
    if extract_name:
        data = data.filter(extract__name__icontains=extract_name)
    if micro_name:
        data = data.filter(micro__name__icontains=micro_name)

    # Pagination: Show 20 items per page
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'data': page_obj,
        'extract_name': extract_name,
        'micro_name': micro_name
    }
    return render(request, 'main/extracts.html', context)

def contact_page(request):
    return render(request, 'main/contact.html')
