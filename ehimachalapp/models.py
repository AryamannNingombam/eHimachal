from django.db import models

# Create your models here.
class DestinationCategory(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50,unique = True)

    def __str__(self):

        return self.name


class ContactMe(models.Model):
    sno = models.AutoField(primary_key = True)
    email_address = models.EmailField()
    message = models.TextField(blank = False,null=False)
    def __str__(self):
        return self.email_address

class Destination(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50,unique = True)
    description = models.TextField(default='')
    category = models.ManyToManyField(DestinationCategory,blank = True)
    tag = models.CharField(max_length = 50,default = '',blank = True)
    population = models.IntegerField(blank = True,default = 0)
    male_pc = models.IntegerField(blank = True,default = 0)
    female_pc = models.IntegerField(blank = True,default = 0)
    total_educated = models.IntegerField(blank = True,default = 0)
    male_educated  =models.IntegerField(blank = True,default = 0)
    female_educated = models.IntegerField(blank = True,default = 0)
    is_in_homepage = models.BooleanField(default = True)
    content_credit = models.CharField(max_length = 100,blank = False,default = '')
    show_demographics = models.BooleanField(default=True)
    show_hotels = models.BooleanField(default=True)
    show_video = models.BooleanField(default= False)
    show_images = models.BooleanField(default = True)
    def __str__(self):
        return self.name
    
class Image(models.Model):
    sno = models.AutoField(primary_key = True)
    image_source = models.TextField(default = '')
    image_destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    image_url  = models.ImageField(blank= False,upload_to= "DestinationImages/")
    image_online_url = models.CharField(max_length = 1000000,default = '')
    is_title_image = models.BooleanField(default= False)
    def __str__(self):
        return f'{self.name}'


class CategoryPhoto(models.Model):
    sno = models.AutoField(primary_key = True)
    image_destination = models.ForeignKey(DestinationCategory,on_delete=models.CASCADE)
    image_path = models.ImageField(blank = False,upload_to = 'CategoryImages/')
    def __str__(self):
        return self.image_destination.name


class Accomodation(models.Model):
    sno  = models.AutoField(primary_key = True)
    accomodation_destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    name= models.CharField(max_length = 50)
    accomodation_image = models.URLField()
    website_url  = models.CharField(max_length= 100000,blank = True)

    def __str__(self):
        return self.name

class DestinationVideo(models.Model):
    sno  = models.AutoField(primary_key = True)
    video_destination  = models.OneToOneField(Destination,on_delete=models.CASCADE)
    video_link = models.URLField()

    def __str__(self):
        return self.video_destination.name


class ContactForError(models.Model):
    sno = models.AutoField(primary_key = True)
    email = models.EmailField(blank = False)
    message = models.TextField(blank = False)
    image = models.ImageField(blank = True,upload_to='ErrorComplaints/')

    def __str__(self):
        return self.email