from django.shortcuts import render,HttpResponse,redirect,reverse
from .models import DestinationCategory,Destination,Image,ContactMe,CategoryPhoto,Accomodation,DestinationVideo,ContactForError
from django import forms
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .Serializers import ContactMeSerializer
from django.core.paginator import Paginator
#FORMS 


class ContactForm(forms.Form):
    email = forms.EmailField(label = 'Email',widget = forms.EmailInput( attrs = {'id' : 'email', 'name' : 'email','class' : 'form-control formStyle','placeholder' : 'Enter Email','required' : 'true'}))
    content = forms.CharField(label = 'Content',widget = forms.Textarea(attrs = {'id' : 'content','name' : 'content','class' : 'form-control formStyle','rows' : '10','required' : 'true' }))
class ContactErrorForm(forms.Form):
    email = forms.EmailField(label = 'Enter Your Email',widget = forms.EmailInput( attrs = {'id' : 'email', 'name' : 'email','class' : 'form-control formStyle','placeholder' : 'Enter Email','required' : 'true'}))
    content = forms.CharField(label = 'Describe The Bug',min_length=5,widget = forms.Textarea(attrs = {'id' : 'content','name' : 'content','class' : 'form-control formStyle','rows' : '10','required' : 'true' }))
    image= forms.FileField(required = False,widget =  forms.FileInput(attrs={"id" : 'image','name' : 'image','accept' : 'image/*'}))
    

#For Navbar
categories = DestinationCategory.objects.all()
# Create your views here.

def home(requests):

    all_destinations = Destination.objects.filter(is_in_homepage = True)
    all_destinations2 = Destination.objects.filter(is_in_homepage = False)
    #this array would contain the main image of the destination and the name of the destination
    destination_array_to_send = []
    destination_array_to_send2 = []
    for destination in all_destinations:
        destination_main_photo = Image.objects.get(image_destination = destination,is_title_image = True)
        #Appending to list
        destination_array_to_send.append([destination,destination_main_photo])
    for destination in all_destinations2:
            destination_main_photo = Image.objects.get(image_destination = destination,is_title_image = True)
        #Appending to list
            destination_array_to_send2.append([destination,destination_main_photo])


    return render(requests,'homepage/homepage.html',{'categories' : categories,'destinations' : destination_array_to_send,'destinations2' : destination_array_to_send2})


def history(requests):
    return render(requests,'history/history.html',{'categories' : categories})


def destination_places(requests,sno):
    
    destination_to_see = Destination.objects.get(sno = sno)

    main_image = Image.objects.get(image_destination = destination_to_see,is_title_image= True)
    all_images = Image.objects.filter(image_destination = destination_to_see,is_title_image = False)
    if destination_to_see.show_video:
        video = DestinationVideo.objects.get(video_destination = destination_to_see)
        return render(requests,'Destination/place.html',{'categories' : categories,'destination' : destination_to_see,'images' : all_images,'main_image' : main_image,'video' : video})

    else:
        return render(requests,'Destination/place.html',{'categories' : categories,'destination' : destination_to_see,'images' : all_images,'main_image' : main_image})

def destination_category(requests,category):    
    cat = DestinationCategory.objects.get(name = category)
    category_destinations = Destination.objects.filter(category = cat)
    main_image = CategoryPhoto.objects.filter(image_destination = cat)[0]

    dest_image_union = []
    for destination in category_destinations:
        dest_image_union.append([destination,Image.objects.get(image_destination = destination,is_title_image= True)])

    return render(requests,'Destination/category.html',{'categories' : categories,'destinations' : dest_image_union,'title' : category,'main_image' : main_image})


def contact(requests):
    new_form = ContactForm()
    return render(requests,'contact/contact.html',{'categories' : categories,'form' : new_form,'is_contact_form' : True})
            

def accomodations(requests):
    all_destinations= Destination.objects.filter(show_hotels = True)
    dest_image_union = []
    for destination in all_destinations:
        dest_image_union.append([destination,Image.objects.get(image_destination = destination,is_title_image= True)])
    paginator = Paginator(dest_image_union,6) 
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(requests,'accomodations/accomodations.html',{'categories' : categories,'destinations' : dest_image_union,'page_obj': page_obj})


def accomodation_specific(requests,sno):
    destination = Destination.objects.get(sno = sno)
    if destination.show_hotels : 
        accomodations = Accomodation.objects.filter(accomodation_destination = destination)
        return render(requests,'accomodations/places.html',{'categories' : categories,'destination' : destination,'accomodations' : accomodations})
    else:
        messages.info(requests,"<strong>HELLO!</strong><p>The page you're looking for doesn't exist!</p>")
        return redirect(reverse('homepage'),{'categories' : categories})

def issue(requests):

    form = ContactErrorForm()
    return render(requests,'contact/contact-error.html',{'categories' : categories,'form' : form,'is_contact_form' : True})


#API'S
@api_view(['POST','GET'])
def contactRequest(requests):
    if requests.method == 'POST':

        serializer = ContactMeSerializer(data  = requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'successful': True})
        else:
            return Response({'successful': False})

    messages.warning(requests,"<strong>HEY!</strong> You are <strong>not authenticated</strong> to access the page you requested for.<strong> Sorry!</strong>")
    return redirect(reverse('homepage'),{'categories' : categories})


def issue_request(requests):
   if requests.method == "POST":
       email = requests.POST.get('email')
       content = requests.POST.get('content')
       image = requests.FILES.get('image')
       form_check = ContactErrorForm(requests.POST,requests.FILES)
       if form_check.is_valid():
            new_contact = ContactForError(email = email,message = content,image = image)
            new_contact.save()
            messages.success(requests,'<strong>Hello!</strong> We Have <strong>Got Your Complaint</strong> And Would Try To Fix The Bug As Soon As We Can. <strong>Thank You!</strong> ')
            return redirect(reverse('issue'),{'categories' : categories,'form' : ContactErrorForm()})


       else:
            messages.error(requests,'<strong>Hello!</strong>We Seem To <strong>Have Some Problems Getting Your Form </strong> . Please Make Sure That You Have Entered Everything Right. <strong>Thank You!</strong> ')
            return redirect(reverse('issue'),{'categories' : categories,'form' : ContactErrorForm()})



