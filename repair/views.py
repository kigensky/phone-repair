from cloudinary.models import CloudinaryField
from django.shortcuts import render,redirect
from repair.models import Profile, Repair
from repair.forms import ProfileForm, RepairForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    repairs = Repair.objects.all()
    ctx = {'repairs':repairs}
    
    return render (request, 'repair/repair_list.html', ctx )
    
@login_required    
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

@login_required    
def repairDelete(request, id):
    repair = Repair.objects.get(pk=id)
    
    repair.delete()
    
    messages.success(request, 'Successfully deleted.')
    return redirect('repair-home')
    
@login_required    
def repairUpdate(request,id):
    repair = Repair.objects.get(pk=id)
    
    form = RepairForm(instance=repair)
    
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            RepairForm.objects.filter(pk=id).update(title=form.cleaned_data['title'], 
            description=form.cleaned_data['description'], 
            subject_id=form.cleaned_data['subject'])
        
            messages.success(request, 'Successfully updated.')
            return redirect('repair-home')
    
    ctx = {'form':form}
    
    return render(request,'repair/repair_form.html', ctx)
    
def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            # send_welcome_email(form.cleaned_data['username'], form.cleaned_data['email'])

            messages.success(request, 'Successful Registration.')

            return redirect('login')

    return render(request,'repair/registration/register.html',{'form':form})     
    
@login_required
def profile(request):
    user = request.user

    return render(request,'reprofile/profile.html', {'user':user})


@login_required
def addprof(request,id):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)

        file_to_upload = request.FILES['profile_photo']

        if form.is_valid():
            upload_result = CloudinaryField.uploader.upload(file_to_upload)
            new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            profile = Profile(profile_photo=new_result,
                              bio=form.cleaned_data['bio'],
                              user=request.user)

            profile.save_profile()

            messages.success(request, 'Successful profile creation.')
            return redirect('profile')

    ctx = {'form':form}

    return render(request,'profile/update.html',ctx)



def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text    