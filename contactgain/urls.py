from django.urls import path,include
from .views import contactFormView, homeView, proofView, ContactListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contactapi',ContactListViewSet,basename='ContactList')

urlpatterns = [
	path('addcontact/', contactFormView, name='ContactFormUrl'),
	path('home/',homeView,name='HomeViewUrl'),
	path('proof',proofView, name='ProofUrl'),
	path('',include(router.urls)),
]