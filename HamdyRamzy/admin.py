from django.contrib import admin

# Register your models here.
from .models import Owner, Contact, SocialMedia, Skill, Certificate, Work, BlogPost, ProjectPost

admin.site.register(Owner)
admin.site.register(Contact)
admin.site.register(SocialMedia)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Work)
admin.site.register(BlogPost)
admin.site.register(ProjectPost)
