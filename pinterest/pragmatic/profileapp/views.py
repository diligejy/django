from profileapp.decorators import profile_ownership_required
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileCreationForm
from django.urls import reverse_lazy
# Create your views here.
from django.utils.decorators import method_decorator


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 임시 저장
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'
