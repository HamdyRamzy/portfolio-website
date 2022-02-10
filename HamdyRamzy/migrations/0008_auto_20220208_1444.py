# Generated by Django 3.2.8 on 2022-02-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamdyRamzy', '0007_auto_20220201_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
                ('subject', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='language',
            name='Proficiency',
            field=models.CharField(blank=True, choices=[('elementary proficiency', 'elementary proficiency'), ('full professional proficiency', 'full professional proficiency'), ('limited working proficiency', 'limited working proficiency'), ('native or bilingual proficiency', 'native or bilingual proficiency'), ('professional working proficiency', 'professional working proficiency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Full time', 'Full time'), ('Part time', 'Part time'), ('Internship', 'Internship'), ('Freelancer', 'Freelancer')], max_length=300, null=True),
        ),
    ]