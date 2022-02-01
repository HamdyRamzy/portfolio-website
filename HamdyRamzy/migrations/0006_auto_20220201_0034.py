# Generated by Django 3.2.8 on 2022-01-31 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamdyRamzy', '0005_auto_20220131_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='Proficiency',
            field=models.CharField(blank=True, choices=[('elementary proficiency', 'elementary proficiency'), ('limited working proficiency', 'limited working proficiency'), ('native or bilingual proficiency', 'native or bilingual proficiency'), ('full professional proficiency', 'full professional proficiency'), ('professional working proficiency', 'professional working proficiency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Part time', 'Part time'), ('Internship', 'Internship'), ('Freelancer', 'Freelancer'), ('Full time', 'Full time')], max_length=300, null=True),
        ),
    ]
