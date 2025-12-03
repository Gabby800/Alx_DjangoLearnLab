from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created succesfully! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserForm()

    return render(request, 'blog/register.html', {'form': form})


#User registration and forms update views
@login_required
def profile(request):
    user = request.user
    profile = user.profile  # OneToOne relation
    
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = CustomUserForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'blog/profile.html', context)
