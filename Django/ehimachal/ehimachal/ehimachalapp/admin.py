from django.contrib import admin
from .models import DestinationCategory,Destination,Image,ContactMe,CategoryPhoto,Accomodation,DestinationVideo,ContactForError
# Register your models here.

    
class ImageAdmin(admin.ModelAdmin):
    list_display  = ('name','image_destination')

@admin.register(Destination)
class DescriptionAdminMCE(admin.ModelAdmin):
    class Media:
        js = ('/static/Script/TinyMCE.js',)

        css = {
             'all': ('/static/css/test.css',)
        }
    filter_horizontal = ('category',)


class AccomodationAdmin(admin.ModelAdmin):
    list_display = ('name','accomodation_destination')



admin.site.register(Accomodation,AccomodationAdmin)



admin.site.register(DestinationCategory)
admin.site.register(ContactMe)
admin.site.register(CategoryPhoto)
admin.site.register(DestinationVideo)
admin.site.register(ContactForError)

admin.site.register(Image,ImageAdmin)

