from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm, UserImageUpload
from .models import Profile, Chat, Board
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
def index(request):
	#template = loader.get_template('/index.html')
	if request.method == 'GET':
		return render(request, 'index.html',)
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)

		if user is not None:
			#if user exists
			login(request,user)
			return render(request,'index.html', {'login_message': 'Welcome ' + username +'!'})
		else:
			#if user doesn't exist.
			return render(request, 'index.html', {'login_message':"Incorrect username or password"})


def people(request):
	if request.method == 'GET':
		w2017 = Profile.objects.filter(session = "2017 Winter")
		s2017 = Profile.objects.filter(session = "2017 Summer")
		w2016 = Profile.objects.filter(session = "2016 Winter")

		return render(request, 'people.html', {'w2017':w2017, 's2017': s2017, 'w2016':w2016})
	else:
		model = Profile
		name = request.POST['name']
		school = request.POST['school']
		github = request.POST['github']
		specialty = request.POST['specialty']
		url = request.POST['url']
		quote = request.POST['quote']
		session = request.POST['session']
		profile = Profile(name = name, school = school, url = url, specialty = specialty, github = github, quote = quote, session = session)
		profile.save()

		w2017 = Profile.objects.filter(session = "2017 Winter")
		s2017 = Profile.objects.filter(session = "2017 Summer")
		w2016 = Profile.objects.filter(session = "2016 Winter")

		return render(request, 'people.html', {'w2017':w2017, 's2017': s2017, 'w2016':w2016})


def board(request):
	if request.method == "POST":
		form = UserImageUpload(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			b = Board.objects.all()
			return render(request, 'board.html', {'form': form,'board':b})
	else:	
		form = UserImageUpload()
		b = Board.objects.all()
		return render(request, 'board.html', {'form':form,'board':b})


#chat = home 
#rest is same
def chat(request):
	c = Chat.objects.all()
	return render(request, "chat.html", {'home':'active', 'chat':c})

def post(request):
	if request.method == "POST":
		msg = request.POST.get('msgbox',None)
		c = Chat(user = request.user, message = msg)
		if msg != '' or msg != None:
			c.save()
		return JsonResponse({'msg': msg, 'user': c.user.username})
	else:
		return HttpResponse('Request must be POST.')

def messages(request):
	c = Chat.objects.all()
	return render(request, 'messages.html', {'chat':c})


def gallery(request):
	return render(request, 'gallery.html')
	#model = something
	#template_name = "something.html"

def add_profile(request):
	return	


class UserFormView(View):
	form_class = UserForm
	template_name = 'registration_form.html'

	# display blank form- new user registering
	def get(self,request):
		if request.user.is_authenticated:
			logout(request)
			return render(request, 'index.html')
		else:
			form = self.form_class(None)
			return render(request, self.template_name, {'form': form})

	#process form data
	def post(self,request):
		form = self.form_class(request.POST)	#context is just for passing data.

		if form.is_valid():

			user = form.save(commit=False)	#doesn't save to database yet.

			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct
			user = authenticate(username = username, password = password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('index')

		return render(request, self.template_name, {'form':form})