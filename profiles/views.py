from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.

def store_file(file):
    with open('img/image.jpg', "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES['image'])
        return HttpResponseRedirect("/profiles")

