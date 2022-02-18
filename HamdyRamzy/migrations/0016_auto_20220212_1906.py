# Generated by Django 3.2.8 on 2022-02-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamdyRamzy', '0015_auto_20220212_1901'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteConfig',
            new_name='SiteInfo',
        ),
        migrations.AlterField(
            model_name='language',
            name='Proficiency',
            field=models.CharField(blank=True, choices=[('elementary proficiency', 'elementary proficiency'), ('native or bilingual proficiency', 'native or bilingual proficiency'), ('professional working proficiency', 'professional working proficiency'), ('limited working proficiency', 'limited working proficiency'), ('full professional proficiency', 'full professional proficiency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Internship', 'Internship'), ('Part time', 'Part time'), ('Full time', 'Full time'), ('Freelancer', 'Freelancer')], max_length=300, null=True),
        ),
    ]
