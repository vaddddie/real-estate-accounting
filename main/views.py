from django.shortcuts import render, redirect
from .forms import BuildingForm
from .models import Building
from django.views.generic.edit import UpdateView

def createBuilding(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else: 
            print(form.errors)
    else:
        form = BuildingForm()
    return render(request, 'main/createBuilding.html', {'form': form})
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
            queryset = queryset.filter(objArea__gte=min_area, objArea__lte=max_area)
        elif min_area:
            queryset = queryset.filter(objArea__gte=min_area)
        elif max_area:
            queryset = queryset.filter(objArea__lte=max_area)
        
        if (state!="Любой"):
            queryset = queryset.filter(objState=state)
        if (tp!="Любое"):
            queryset = queryset.filter(objType=tp)
        if (status!="Любое"):
            queryset = queryset.filter(objStatus=status)
    context = {
        'buildings': queryset,
    }
    print(context)
    return render(request, 'main/index.html', context)

def edit_building(request):
    if request.method == 'POST':
        building_id = request.POST.get('building_id')
        return redirect("/editBuilding/"+str(building_id))
    return render(request, 'main/editBuilding.html')
    
class BuildingUpdateView(UpdateView):
    model = Building
    form_class = BuildingForm
    #fields = ['objState', 'objDistrict', 'objAddress', 'objType', 'objStatus', 'objArea', 'objOwner', 'objUser', 'objImage']
    template_name_suffix = '_update_form'
    success_url= '/'