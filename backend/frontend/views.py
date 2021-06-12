from django.shortcuts import render

# Create your views here.
def home_view(request):
	#print(request.GET)
	return render(request,"home.html")