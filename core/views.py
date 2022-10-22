from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserChangeForm
from core.forms import EditProfileForm
from django.urls import is_valid_path

# Create your views here.

@login_required
def edit_user_details(request):
    """A page for the user to view and update their details."""
    # user = get_object_or_404(user, id=request.user)

    page_title = 'Name'

    if request.method != 'POST':
        form = EditProfileForm(instance=request.user)
        message = ''
    else:
        form = EditProfileForm(instance=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            message = 'Details saved'

    context = {'user': request.user, 'message': message, 'form': form, 'page_title': page_title }

    return render(request, "edit_user_details.html", context )