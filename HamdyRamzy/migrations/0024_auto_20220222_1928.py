# Generated by Django 3.2.8 on 2022-02-22 17:28

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('HamdyRamzy', '0023_auto_20220220_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_picture',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='blog post pictures/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='organization_logo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='organization logos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='language',
            name='Proficiency',
            field=models.CharField(blank=True, choices=[('native or bilingual proficiency', 'native or bilingual proficiency'), ('elementary proficiency', 'elementary proficiency'), ('professional working proficiency', 'professional working proficiency'), ('full professional proficiency', 'full professional proficiency'), ('limited working proficiency', 'limited working proficiency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project_image',
            name='picture',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='project pictures/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='projectpost',
            name='post_picture',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='project post pictures/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='work',
            name='company_logo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='company logos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='work',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Freelancer', 'Freelancer'), ('Full time', 'Full time'), ('Internship', 'Internship'), ('Part time', 'Part time')], max_length=300, null=True),
        ),
    ]
