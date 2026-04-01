from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProfileForm


@login_required
def profile_detail(request):
    profile = request.user.profile
    return render(request, "accounts/profile_detail.html", {"profile": profile})


@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_detail")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/profile_edit.html", {"form": form})