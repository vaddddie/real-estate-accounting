from django.shortcuts import render, redirect
from .forms import BuildingForm
from .models import Building
from django.views.generic.edit import UpdateView
import xml.etree.ElementTree as ET

def createBuilding(request):
    if request.method == 'POST':
        xml_file = request.FILES.get('xml-file')
        if xml_file is not None:
            xml_file = ET.parse(xml_file)
            values = {'objState': None, 'objDistrict': None, 'objAddress': None, 'objType': None, 'objStatus': None,
                      'objArea': None, 'objOwner': None, 'objUser': None, 'objImage': None}
            for field in xml_file.iter('field'):
                values[field.get('name')] = field.text
            new_obj = Building(
                objState=values['objState'],
                objDistrict=values['objDistrict'],
                objAddress=values['objAddress'],
                objType=values['objType'],
                objStatus=values['objStatus'],
                objArea=values['objArea'],
                objOwner=values['objOwner'],
                objUser=values['objUser'],
                objImage=values['objImage'])
            new_obj.save()
            return redirect('/')
        else:
            form = BuildingForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else: 
                print(form.errors)
            return redirect("/")
    else:
        form = BuildingForm()
    return render(request, 'main/createBuilding.html', {'form': form})

def filterBuilding(request):
    queryset = Building.objects.all()    
    if request.method == 'POST':
        min_area = request.POST.get('min_area')
        max_area = request.POST.get('max_area')
        state = request.POST.get('state')
        tp = request.POST.get('type')
        status = request.POST.get('status')
        print(state)

        if min_area and max_area:
            queryset = queryset.filter(objArea__gte=min_area, objArea__lte=max_area)
        elif min_area:
            queryset = queryset.filter(objArea__gte=min_area)
        elif max_area:
            queryset = queryset.filter(objArea__lte=max_area)
        
        if (state!="Любой") & (state!=None) :
            queryset = queryset.filter(objState=state)
        if (tp!="Любое") & (tp!=None):
            queryset = queryset.filter(objType=tp)
        if (status!="Любое") & (status!=None):
            queryset = queryset.filter(objStatus=status)
    context = {
        'buildings': queryset,
    }
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
