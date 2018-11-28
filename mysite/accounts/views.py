from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
@csrf_exempt
def signup_view(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid(): #validate log in
		   form.save()
		   #log the user in
		   #login(request,user)
		return redirect('accounts:userlogin')
			#create a userlogin url in mysite
	else:
		form = UserCreationForm()
	return render(request, "accounts/createaccount.html", {'form': form})

@csrf_exempt
def user_login(request):
	return render(request, "accounts/userlogin.html")

@csrf_exempt
def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		#if valid log in user
		if form.is_valid():
			user = form.get_user()
			login(request, user)
		return redirect(reverse('accounts:userlogin')) #need login page url
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {"form": form})
@csrf_exempt
def logout_view(request):
	if request.method=="POST":
		logout(request)
		return redirect("accounts:login")
