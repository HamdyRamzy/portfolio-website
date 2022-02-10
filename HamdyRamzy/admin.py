from django.contrib import admin

# Register your models here.
from .models import  Owner, Contact, SocialMedia, Skill, Language, Certificate, Work, BlogPost, ProjectPost, ContactMe

admin.site.register(Owner)
admin.site.register(Contact)
admin.site.register(SocialMedia)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Certificate)
admin.site.register(Work)
admin.site.register(BlogPost)
admin.site.register(ProjectPost)
admin.site.register(ContactMe)