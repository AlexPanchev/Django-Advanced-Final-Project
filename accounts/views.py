from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProfileForm, RegisterForm


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


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("profile_detail")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)