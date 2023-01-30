from django.shortcuts import render,redirect
from .models import Contact, Proof, Level
from .forms import ContactForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ContactList
from django.contrib.auth.decorators import login_required

def contactFormView(request):
	form = ContactForm
	level = Level.objects.get(level_number=0)
	user_contact = User.objects.get(username=request.user)

	if request.method == 'POST':
		number = request.POST.get('phonenumber')
		contact = Contact.objects.get(user=user_contact)
		contact.phone= number
		contact.save()
		return redirect('HomeViewUrl') 

	template = 'account/contactform.html'
	context = dict(form=form)
	return render(request,template,context)

@login_required
def homeView(request):
	user = User.objects.get(username=request.user)
	contact = Contact.objects.get(user=user)
	proof_count = Proof.objects.filter(owner=contact,active=True)
	my_contact = list(contact.contact_list.all())
	level = Level.objects.get(level_number=contact.level.level_number)
	levels = Level.objects.all().exclude(level_number=0)
	if contact.level.download_link:
		download = True
	else:
		download = False
	context = dict(contact=contact,my_contact=my_contact,proof_count=proof_count,download=download,level=level,levels=levels)
	return render(request,'contactTemplate/home.html',context)

def getContact(request,x):
	pass

def proofView(request):
	user = User.objects.get(username=request.user)
	contact = Contact.objects.get(user=user)

	if request.method == 'POST':
		files = request.FILES.getlist('file')
		for file in files:
			a = Proof.objects.create(owner=contact,image=file)
			a.save()

	return redirect('HomeViewUrl')

class ContactListViewSet(viewsets.ModelViewSet):
	serializer_class = ContactList
	#queryset = Contact.objects.get(user=lambda request:User.objects.get(username=request.user).id)
	def get_queryset (self):
		user = User.objects.get(username=self.request.user)
		contact = Contact.objects.get(user=user)
		my_contact = contact.contact_list.all()
		return my_contact
