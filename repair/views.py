from django.shortcuts import render,redirect
from repair.models import Repair
from repair.forms import RepairForm
from django.contrib import messages
# Create your views here.

def home(request):
    cards = Repair.objects.all()
    ctx = {'repair':cards}
    
    return render (request, 'repair/repair_list.html', ctx )
    
def repairCreateView(request):
    form = RepairForm()
    
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
        
            messages.success(request, 'Successfully Added.')
            return redirect('repair-home')
    
    ctx = {'form':form}
    
    return render(request,'repair/repair_form.html', ctx)    