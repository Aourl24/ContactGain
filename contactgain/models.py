from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from DjReact.settings import BASE_DIR
from django.http import HttpResponse, FileResponse
from django.utils.html import mark_safe

class Level(models.Model):
	level_number = models.IntegerField(default=0,unique=True)
	proof = models.IntegerField(default=3)
	maximum_contact = models.IntegerField(default=0)
	download_link = models.BooleanField(default=False)

	def __str__(self):
		return f'Level {self.level_number}'

class Contact(models.Model):
	user = models.OneToOneField(User,related_name='contact',on_delete=models.CASCADE)
	phone = models.IntegerField(default=int('+234'))
	email = models.EmailField(null=True,blank=True)
	date_joined = models.DateField(auto_now_add=True,blank=True,null=True)
	level = models.ForeignKey(Level,related_name='contact',on_delete=models.SET_NULL,null=True,blank=True)
	contact_list = models.ManyToManyField('self',symmetrical=True,null=True,blank=True)

	def __str__(self):
		return self.user.username.title()

	def newProof(self):
		proof = Proof.objects.filter(owner=self)
		for pro in proof:
			if pro.active == False:
				return mark_safe(f'<span>Pending</span>') 
			else:
				pass

	class Meta:
		ordering = ['pk']

	def synchronize(self):
		path = str(BASE_DIR.joinpath('media'))
		file_name=f'{path}/{self.user.username}contactList.vcf'
		con = self.contact_list.all()
		with open(file_name,'w+') as file_obj:
			for contact in con:
				file_obj.write(f"BEGIN:VCARD \nVERSION:3.0 \nN:{contact.user.username};{contact.user.username};;;\nFN:{contact.user.username}\n\
TEL;type=CELL;type=pref:0{contact.phone}\n\
END:VCARD\n\
")
		return f'media/{self.user.username}contactList.vcf'


class Proof(models.Model):
	storage = 'The'
	owner = models.ForeignKey(Contact, related_name='proof', on_delete=models.CASCADE)
	image = models.ImageField(upload_to=f'{storage} proof/',null=True,blank=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.owner.user.username} proof '

	def im(self):
		return f'{self.owner.user.username}'

	def  img_preview(self):
		return mark_safe(f"<img src='{self.image.url}' width='250px' height='400px'>")


@receiver(post_save, sender=Proof)
def ProofCreated(instance,sender,created,**kwargs):
	con = Contact.objects.all().order_by('level__level_number')
	prof=Proof.objects.filter(owner=instance.owner.id,active=True)
	owner_contact = Contact.objects.get(user=instance.owner.user.id)
	print(prof)

	if len(list(prof)) >= owner_contact.level.proof:
		for contact in con[:owner_contact.level.maximum_contact]:
			owner_contact.contact_list.add(contact)
			owner_contact.save()
		up_level=Level.objects.get(level_number=owner_contact.level.level_number +1)
		owner_contact.level = up_level
		print(owner_contact.level.level_number)
		owner_contact.save()


@receiver(pre_save,sender=Proof)
def checkProof(instance,sender,**kwargs):
	if instance.id is None:
		pass
	else:
		instance.storage = str(instance.owner.user.username)
	
@receiver(post_save,sender=User)
def createContact(instance,sender,created,**kwargs):
	if created:
		try:
			level = Level.objects.get(level_number=0)
		except:
			level = Level.objects.create()
		Contact.objects.create(user=instance,level=level)