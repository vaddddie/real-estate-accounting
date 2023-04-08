from django.shortcuts import render, redirect
from .forms import BuildingForm
from .models import Building

#def test(request):
#    return render(request, 'main/index.html')

def createBuilding(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = BuildingForm()
    return render(request, 'main/createBuilding.html', {'form': form})

def filterBuilding(request):
    queryset = Building.objects.all()
    print(Building.objects.all())
    
    if request.method == 'POST':
        min_area = request.POST.get('min_area')
        max_area = request.POST.get('max_area')
        state = request.POST.get('state')
        tp = request.POST.get('type')
        status = request.POST.get('status')
        print(queryset[0].objImage)

        if min_area and max_area:
            queryset = queryset.filter(area__gte=min_area, area__lte=max_area)
        elif min_area:
            queryset = queryset.filter(area__gte=min_area)
        elif max_area:
            queryset = queryset.filter(area__lte=max_area)
        
        if state:
            queryset = queryset.filter(objState=state)
        if tp:
            queryset = queryset.filter(objType=tp)
        if status:
            queryset = queryset.filter(objStatus=status)
    context = {
        'buildings': queryset,
    }
    print(context)
    return render(request, 'main/index.html', context)
