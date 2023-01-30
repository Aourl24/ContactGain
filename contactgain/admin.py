from django.contrib import admin
from .models import Contact,Proof,Level

#class ProofModel(admin.ModelAdmin):
#	read_only_fields
admin.site.register([Proof,Level])

class InlineProof(admin.TabularInline):
	model = Proof
	extra = 0
	readonly_fields = ['img_preview']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	readonly_fields = ['phone','user','email']
	list_display = ['user','pk','phone','newProof']
	inlines = [InlineProof]