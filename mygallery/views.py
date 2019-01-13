from django.shortcuts import render
#导入gallery app
from gallery.models import Gallery



def home(request):
	frontgallery = Gallery.objects
	return render(request, 'home.html', {'frontgallery':frontgallery})
