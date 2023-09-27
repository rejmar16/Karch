from django.contrib import admin
from .models import Project, Project_Photo, Contact
# Register your models here.

class ProjectPhotoInLine(admin.TabularInline):
    model = Project_Photo
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info',    {'fields' : ['name','type','text']}),
        ('Photo', {'fields' : ['screen']}),
        ('Date information', {'fields' : ['published_date']}),
    ]
    inlines = [ProjectPhotoInLine]
    list_display = ('name' , 'type','published_date')
    list_filter = ['published_date']
    search_fields = ['name']

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields' : ['first_name','last_name']}),
        ('Photo', {'fields' : ['photo']}),
        ('Contacts', {'fields': ['email','phone']}),
        ('Text', {'fields': ['text']})
    ]
#admin.site.register(Introduction, IntroductionAdmin)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)