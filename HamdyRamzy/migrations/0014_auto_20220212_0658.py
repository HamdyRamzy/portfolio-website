# Generated by Django 3.2.8 on 2022-02-12 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamdyRamzy', '0013_auto_20220212_0655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='views',
            new_name='viewer',
        ),
        migrations.AlterField(
            model_name='language',
            name='Proficiency',
            field=models.CharField(blank=True, choices=[('limited working proficiency', 'limited working proficiency'), ('professional working proficiency', 'professional working proficiency'), ('elementary proficiency', 'elementary proficiency'), ('native or bilingual proficiency', 'native or bilingual proficiency'), ('full professional proficiency', 'full professional proficiency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Freelancer', 'Freelancer'), ('Part time', 'Part time'), ('Internship', 'Internship'), ('Full time', 'Full time')], max_length=300, null=True),
        ),
    ]