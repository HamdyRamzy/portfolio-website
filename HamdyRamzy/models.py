from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create owner model.
class Owner(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(null=True, blank=True, max_length=50)
    bio = models.CharField(null=True, blank=True, max_length=300)
    about = models.TextField(null=True, blank=True, max_length=1000)
    birthday = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    photo = models.ImageField(null=True, blank=True, upload_to='my photos/%y/%m/%d')
    updated_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

# Create contact model.
class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contact', on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=50)
    icon = models.CharField(null=True, blank=True, max_length=300)
    information = models.CharField(null=True, blank=True, max_length=150)
    
    def __str__(self):
        return self.name

# Create social media model.
class SocialMedia(models.Model):
    user = models.ForeignKey(User, related_name='socialmedia', on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=50)
    icon = models.CharField(null=True, blank=True, max_length=300)
    url = models.URLField(null=True, blank=True, max_length=200)
    
    def __str__(self):
        return self.name

# Create skill model.
class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skill', on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=150)
    
    def __str__(self):
        return self.name


# Create Language Proficiency choices.
Proficiency = {
    ('elementary proficiency', 'elementary proficiency'),
    ('limited working proficiency', 'limited working proficiency'),
    ('professional working proficiency', 'professional working proficiency'),
    ('full professional proficiency', 'full professional proficiency'),
    ('native or bilingual proficiency', 'native or bilingual proficiency'),
}


# Create language model.
class Language(models.Model):
    user = models.ForeignKey(User, related_name='language', on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=150)
    Proficiency = models.CharField(null=True, blank=True, choices=Proficiency, max_length=200)
    
    def __str__(self):
        return self.name


# Create certificate model.
class Certificate(models.Model):
    user = models.ForeignKey(User, related_name='certificate', on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=300)
    issue_organization = models.CharField(null=True, blank=True, max_length=300)
    organization_logo = models.ImageField(null=True, blank=True, upload_to='organization logos/%y/%m/%d')
    issue_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    credential_id = models.CharField(null=True, blank=True, max_length=300)
    credential_url = models.URLField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.title

# Create employment type choices.
employment_type = {
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
    ('Freelancer', 'Freelancer'),
    ('Internship', 'Internship'),
}


# Create work model.
class Work(models.Model):
    user = models.ForeignKey(User, related_name='work', on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=500)
    employment_type = models.CharField(choices=employment_type, null=True, blank=True, max_length=300)
    company_logo = models.ImageField(null=True, blank=True, upload_to='company logos/%y/%m/%d')
    company_name = models.CharField(null=True, blank=True, max_length=500)
    start_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    description = models.TextField(null=True, blank=True, max_length=1000)


    def __str__(self):
        return self.title


# Create Blog Post model.
class BlogPost(models.Model):
    user = models.ForeignKey(User, related_name='BlogPost', on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=400)
    description = models.CharField(null=True, blank=True, max_length=1000)
    content = RichTextUploadingField()
    post_picture = models.ImageField(null=True, upload_to='blog post pictures/%y/%m/%d')
    uploaded_date = models.DateField(null=True, blank=True)
    tags = TaggableManager()
    time = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# Create Blog Post model.
class ProjectPost(models.Model):
    user = models.ForeignKey(User, related_name='ProjectPost', on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=400)
    description = models.CharField(null=True, blank=True, max_length=1000)
    content = RichTextUploadingField()
    post_picture = models.ImageField(null=True, upload_to='project post pictures/%y/%m/%d')
    uploaded_date = models.DateField(null=True, blank=True)
    tags = TaggableManager()    
    time = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ProjectPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class ContactMe(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email        