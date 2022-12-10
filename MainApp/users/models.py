from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
import random

# Create your models here.

class Resume(models.Model):
    AFRICANAMERICAN = "African American"
    CAUCASIAN = "Caucasian"
    HISPANIC = "Hispanic"
    ASIAN = "Asian"

    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    MARRIED = "Married"
    SINGLE = "Single"
    WIDOWED = "Widowed"
    DIVORCED = "Divorced"

    MIDWEST = "Midwest"
    NORTHEAST = "Northeast"
    MIDATLANTIC = "Mid-Atlantic"
    SOUTHWEST = "Southwest"
    SOUTHEAST = "Southeast"
    NORTHWEST = "Northwest"


    ETHNICITY_CHOICES = [
    (AFRICANAMERICAN, 'African American'),
    (CAUCASIAN, 'Caucasian'),
    (HISPANIC, 'Hispanic'),
    (ASIAN, 'Asian'),
    ]
    SEX_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
    ]
    MARITAL_CHOICES = [
    (MARRIED, 'Married'),
    (SINGLE, 'Single'),
    (WIDOWED, 'Widowed'),
    (DIVORCED, 'Divorced'),
    ]
    REGION_CHOICES = [
    (MIDWEST, 'Midwest'),
    (NORTHEAST, 'Northeast'),
    (MIDATLANTIC, 'Mid-Atlantic'),
    (SOUTHWEST, 'Southwest'),
    (SOUTHEAST, 'Southeast'),
    (NORTHWEST, 'Northwest'),
    ]

    IMAGES = [
        'profile1.jpg',  'profile2.jpg',  'profile3.jpg',  'profile4.jpg',  'profile5.jpg',
        'profile6.jpg',  'profile7.jpg',  'profile8.jpg',  'profile9.jpg',  'profile10.jpg',
    ]

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    uniqueId = models.CharField(null=True, max_length=100)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_images')
    email_confirmed = models.BooleanField(default=False)
    date_birth = models.DateField()
    ethnicity =models.CharField(choices=ETHNICITY_CHOICES, default=AFRICANAMERICAN, max_length=100)
    sex = models.CharField(choices=SEX_CHOICES, default=OTHER, max_length=100)
    marital_status = models.CharField(choices=MARITAL_CHOICES, default=SINGLE, max_length=100)
    addressLine1 = models.CharField(null=True, max_length=200)
    addressLine2 = models.CharField(null=True, max_length=200)
    suburb = models.CharField(null=True, max_length=100)
    city = models.CharField(null=True, max_length=100)
    region = models.CharField(choices=REGION_CHOICES, default=SOUTHEAST, max_length=100)
    phoneNumber = models.CharField(null=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(default= timezone.now)
    last_updated = models.DateTimeField(blank=True, null=True)
    cover_letter = models.FileField(upload_to='resumes')
    cv = models.FileField(upload_to='resumes')


    def __str__(self):
        return '{} {} {}'. format(self.user.first_name, self.user.last_name, self.uniqueId)

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))

        if self.image == 'default.jpg':
            self.image = random.choice(self.IMAGES)


        self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))

        super(Resume, self).save(*args, **kwargs)

class Education(models.Model):
    LEVEL1 = '1 - Highschool Diploma'
    LEVEL2 = '2 - Certificate'
    LEVEL3 = '3 - Bachelors Degree'
    LEVEL4 = '4 - Honors Degree'
    LEVEL5 = '5 - Masters Degree'
    LEVEL6 = '6 - Doctorate Degree'

    LEVEL_CHOICES = [
    (LEVEL1, '1 - Highschool Diploma'),
    (LEVEL2, '2 - Certificate'),
    (LEVEL3, '3 - Bachelors Degree'),
    (LEVEL4, '4 - Honors Degree'),
    (LEVEL5, '5 - Masters Degree'),
    (LEVEL6, '6 - Doctorate Degree'),
    ]

    institution = models.CharField(null=True, blank=True, max_length=200)
    qualification = models.CharField(null=True, blank=True, max_length=200)
    level = models.CharField(choices=LEVEL_CHOICES, default=LEVEL1, max_length=200)
    start_date = models.DateField(blank=True, null=True)
    graduated = models.DateField(blank=True, null=True)
    major_subject = models.CharField(null=True, blank=True, max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return '{} for {} {}'.format(self.qualification, self.resume.user.first_name, self.resume.user.last_name)

class Experience(models.Model):
    company = models.CharField(null=True, blank=True, max_length=200)
    position = models.CharField(null=True, blank=True, max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    experience = models.CharField(blank=True, null=True, max_length=200)
    skills = models.CharField(null=True,blank=True, max_length=200)
    date_created = models.DateTimeField(default = timezone.now)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return '{} at {}'.format(self.position, self.company)
