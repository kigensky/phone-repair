from cloudinary.models import CloudinaryField
from django.shortcuts import render,redirect, get_object_or_404
from repair.models import Profile, Post
from repair.forms import CommentForm, ProfileForm, RepairForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import cloudinary.uploader
# Create your views here.


def home(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}
    
    return render (request, 'repair/repair_list.html', ctx )
    
@login_required    
def repairCreateView(request):
    form = RepairForm()
    
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
        
            messages.success(request, 'Successfully Added.')
            return redirect('post-home')
    
    ctx = {'form':form}
    
    return render(request,'repair/repair_form.html', ctx)   

@login_required    
def repairDelete(request, id):
    repair = Post.objects.get(pk=id)
    
    repair.delete()
    
    messages.success(request, 'Successfully deleted.')
    return redirect('post-home')
    
@login_required    
def repairUpdate(request,id):
    repair = Post.objects.get(pk=id)
    
    form = RepairForm(instance=repair)
    
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            RepairForm.objects.filter(pk=id).update(title=form.cleaned_data['title'], 
            description=form.cleaned_data['description'], 
            subject_id=form.cleaned_data['operating_system'])
        
            messages.success(request, 'Successfully updated.')
            return redirect('post-home')
    
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

    return render(request,'repair/profile/profile.html', {'user':user})


@login_required
def addprof(request,id):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)

        file_to_upload = request.FILES['profile_photo']

        if form.is_valid():
            # # upload_result = CloudinaryField.uploader.upload(file_to_upload)
            # new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dh0tqdg08/')

            # profile = Profile(profile_photo=new_result,
            #                   bio=form.cleaned_data['bio'],
            #                   user=request.user)

            # profile.save_profile()

            messages.success(request, 'Successful profile creation.')
            return redirect('profile')

    ctx = {'form':form}

    return render(request,'repair/profile/update.html',ctx)
  
def post_detail(request, slug):
    template_name = 'repair/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
                                           
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'repair/add_comment_to_post.html', {'form': form})                                           