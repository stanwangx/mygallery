from django.shortcuts import render
from gallery.models import Gallery



def home(request):
	frontgallery = Gallery.objects
	return render(request, 'home.html', {'frontgallery':frontgallery})
