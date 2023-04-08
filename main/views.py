from django.shortcuts import render, redirect
from .forms import BuildingForm

# Create your views here.
# def post(self, request, *args, **kwargs):
#         self.template_name = '/main/index.html'
#         return render(request, self.template_name, self.context)

def test(request):
    return render(request, 'main/index.html')

def createBuilding(request):
    print("createBuilding method called")
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            form.save()
        else:
            print(request.FILES)
            print(form.errors)
    else:
        form = BuildingForm()
    return render(request, 'createBuilding.html', {'form': form})
