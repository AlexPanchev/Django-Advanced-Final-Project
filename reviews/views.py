from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Review
from .forms import ReviewForm


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.dessert_id = self.kwargs["dessert_pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("dessert_detail", kwargs={"pk": self.kwargs["dessert_pk"]})


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("dessert_detail", kwargs={"pk": self.object.dessert.pk})


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("dessert_detail", kwargs={"pk": self.object.dessert.pk})
