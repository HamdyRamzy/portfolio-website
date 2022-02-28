# Generated by Django 3.2.8 on 2022-02-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamdyRamzy', '0017_auto_20220212_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='Proficiency',
            field=models.CharField(blank=True, choices=[('professional working proficiency', 'professional working proficiency'), ('native or bilingual proficiency', 'native or bilingual proficiency'), ('limited working proficiency', 'limited working proficiency'), ('elementary proficiency', 'elementary proficiency'), ('full professional proficiency', 'full professional proficiency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='last_visit',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Part time', 'Part time'), ('Freelancer', 'Freelancer'), ('Full time', 'Full time'), ('Internship', 'Internship')], max_length=300, null=True),
        ),
    ]