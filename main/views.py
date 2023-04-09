<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render, redirect
from .forms import BuildingForm, WorkgroupForm, Login_form
from .models import Building, Workgroup
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
=======
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BuildingForm, EventForm
from .models import Building, Event
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, ListView
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
>>>>>>> calendar
from django.urls import reverse
=======
from django.shortcuts import render, redirect
from .forms import BuildingForm
from .models import Building
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
>>>>>>> parent of 37eaf7a (Added calendar)
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

        if (state != "Любой") & (state != None):
            queryset = queryset.filter(objState=state)
        if (tp != "Любое") & (tp != None):
            queryset = queryset.filter(objType=tp)
        if (status != "Любое") & (status != None):
            queryset = queryset.filter(objStatus=status)
    context = {
        'buildings': queryset,
    }
    return render(request, 'main/index.html', context)


class BuildingUpdateView(UpdateView):
    model = Building
    form_class = BuildingForm
    template_name = 'main/building_update_form.html'
    success_url = '/'

class BuildingDeleteView(DeleteView):
    model = Building
    template_name = "main/building_delete.html"
    success_url = '/'

class BuildingDetailView(DetailView):
    model = Building
    template_name = 'main/building_detail.html'
<<<<<<< HEAD


<<<<<<< HEAD
class WorkgroupCreate(CreateView):
    model = Workgroup
    form_class = WorkgroupForm
    template_name = 'main/workgroup_form.html'
    success_url = '/'
    

class Login(LoginView):
    form_class = Login_form
    template_name = 'main/users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self, **kwargs):
        return reverse("home")

class Logout(LogoutView):
    pass
=======
class CalendarView(ListView):
    model = Event
    template_name = 'main/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'main/event.html', {'form': form})
>>>>>>> calendar
=======
>>>>>>> parent of 37eaf7a (Added calendar)
