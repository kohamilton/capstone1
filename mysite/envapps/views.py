from django.shortcuts import render
from .models import Storm_App, Ossf
from . import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
@login_required(login_url="/accounts/login/")
def storm_apps(request):
	if request.method == 'POST':
		form = forms.envapp_1(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=false) #store info in variable
			instance.projname=request.user #attach project name with logged in user
			instance.save() #commit to db
			return redirect('accounts:userlogin')
	else:
		form = forms.envapp_1() #if criteria not valid return to blank form
	return render(request, 'envapps/stormpermitapp.html', {'form': form})

def ossf_app(request):
	if request.method == 'POST':
		form = forms.envapp_2(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=false)
			instance.owner_fname=request.user
			instance.save()
			return redirect('accounts:userlogin')
	else:
		form = forms.envapp_2()
	return render(request, 'envapps/ossf_app.html', {'form': form})

def app_list(request):
	app_1 = Storm_App.objects.all().order_by('app_date')
	return render(request, 'envapps/stormpermitapp.html', {'app_1': app_1})
