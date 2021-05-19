from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('',views.home,name = 'homepage'),
    path('history/',views.history,name="history"),
    path('destinations/places/<int:sno>',views.destination_places,name="specificPlace"),
    path('destinations/<str:category>',views.destination_category,name="destinations"),
    path('contact/',views.contact,name = 'contact'),
    path('accomodations/places/<int:sno>',views.accomodation_specific,name = 'accomodationSpecific'),
    path('accomodations/',views.accomodations,name = 'accomodations'),
    path('contact-request/',views.contactRequest,name="contact-request"),
    path('contact/issue',views.issue,name= 'issue'),
    path('contact/issue-request',views.issue_request,name= 'issue-request'),

   
    ]
