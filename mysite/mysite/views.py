from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	return render(request, 'accounts/login.html')

#def signup_view(request):
	#if request.method == "POST":
		#form = UserCreationForm(request.POST)
		#if form.is_valid(): #validate log in
		   #user = form.save()
		   #log the user in
		   #login(request,user)

			#return redirect("articles:list")
	#else:
		#form = UserCreationForm()
		#return render(request, "accounts/signup.html", {"form": form})

#def login_view(request):
	#if request.method == "POST":
		#form = AuthenticationForm(data=request.POST)
		#if valid log in user
		#if form.is_valid():
			#user = form.get_user()
			#login(request, user)
			#return redirect('articles:list')
	#else:
		#form = AuthenticationForm()
	#return render(request, 'accounts/login.html', {"form": form})

#def logout_view(request):
	#if request.method == "POST":
		#logout(request)
		#return redirect('articles:list')




#def index(request):
	#return HttpResponse("")
