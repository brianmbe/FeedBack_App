from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from matplotlib import image

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html", {
            "form": ProfileForm()
        })

    def post(self, request):

        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })

