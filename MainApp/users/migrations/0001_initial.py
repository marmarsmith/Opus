# Generated by Django 4.0.3 on 2022-04-29 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('date_birth', models.DateField()),
                ('ethnicity', models.CharField(choices=[('African American', 'African American'), ('Caucasian', 'Caucasian'), ('Hispanic', 'Hispanic'), ('Asian', 'Asian')], default='African American', max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=100)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced')], default='Single', max_length=100)),
                ('addressLine1', models.CharField(max_length=200, null=True)),
                ('addressLine2', models.CharField(max_length=200, null=True)),
                ('suburb', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('region', models.CharField(choices=[('Midwest', 'Midwest'), ('Northeast', 'Northeast'), ('Mid-Atlantic', 'Mid-Atlantic'), ('Southwest', 'Southwest'), ('Southeast', 'Southeast'), ('Northwest', 'Northwest')], default='Southeast', max_length=100)),
                ('phoneNumber', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('cover_letter', models.FileField(upload_to='resumes')),
                ('cv', models.FileField(upload_to='resumes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, max_length=400, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, max_length=200, null=True)),
                ('qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('level', models.CharField(choices=[('1 - Highschool Diploma', '1 - Highschool Diploma'), ('2 - Certificate', '2 - Certificate'), ('3 - Bachelors Degree', '3 - Bachelors Degree'), ('4 - Honors Degree', '4 - Honors Degree'), ('5 - Masters Degree', '5 - Masters Degree'), ('6 - Doctorate Degree', '6 - Doctorate Degree')], default='1 - Highschool Diploma', max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('graduated', models.DateField(blank=True, null=True)),
                ('major_subject', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.resume')),
            ],
        ),
    ]
