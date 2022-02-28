# Generated by Django 3.2.8 on 2022-02-18 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamdyRamzy', '0021_auto_20220218_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='language',
            name='Proficiency',
            field=models.CharField(blank=True, choices=[('native or bilingual proficiency', 'native or bilingual proficiency'), ('limited working proficiency', 'limited working proficiency'), ('elementary proficiency', 'elementary proficiency'), ('professional working proficiency', 'professional working proficiency'), ('full professional proficiency', 'full professional proficiency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Freelancer', 'Freelancer'), ('Part time', 'Part time'), ('Internship', 'Internship'), ('Full time', 'Full time')], max_length=300, null=True),
        ),
    ]