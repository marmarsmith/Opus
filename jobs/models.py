from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from uuid import uuid4


# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    companyLogo = models.ImageField(default='default.png', upload_to='upload_images')
    slug = models.SlugField(max_length=500, null=True, blank=True)
    seeDescription = models.CharField(max_length=500, null=True, blank=True)
    seeKeywords = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('Company {} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('Company {} {}'.format(self.title, self.uniqueId))
        self.seeDescription = 'Apply for {} Jobs on Opus, start your career journey today'.format(self.title)
        self.seeKeywords = '{}, Jobs, Opus, Apply Jobs'.format(self.title)
        super(Company, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    companyLogo = models.ImageField(default='default.png', upload_to='upload_images')
    slug = models.SlugField(max_length=500, null=True, blank=True)
    seeDescription = models.CharField(max_length=500, null=True, blank=True)
    seeKeywords = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))
        self.seeDescription = 'Apply for {} Jobs on Opus, start your career journey today'.format(self.title)
        self.seeKeywords = '{}, Jobs, Opus, Apply Jobs'.format(self.title)
        super(Category, self).save(*args, **kwargs)


class Jobs(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    REMOTE = 'RT'
    NOT_PROVIDED = 'N/A'

    TIER1 = 'Less than 2yrs'
    TIER2 = '2yrs - 5yrs'
    TIER3 = '5yrs - 10 yrs'
    TIER4 = '10yrs - 15yrs'
    TIER5 = 'More than 15yrs'
    NOT_PROVIDED = 'Not Provided'

    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (NOT_PROVIDED, 'N/A'),
        (REMOTE, 'Remote'),
    ]
    EXP_CHOICES = [
        (TIER1, 'Less than 2yrs'),
        (TIER2, '2yrs - 5yrs'),
        (TIER3, '5yrs - 10 yrs'),
        (TIER4, '10yrs - 15yrs'),
        (TIER5, 'More than 15yrs'),
        (NOT_PROVIDED, 'NP')
    ]

    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=100, null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=NOT_PROVIDED)
    experience = models.CharField(max_length=100, choices=EXP_CHOICES, default=NOT_PROVIDED)
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    duties = models.TextField(null=True, blank=True)
    enquiries = models.TextField(null=True, blank=True)
    applications = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    closing_date = models.DateField(null=True, blank=True)
    date_posted = models.DateField(null=True, blank=True)
    contract_type = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=500, null=True, blank=True)
    seeDescription = models.CharField(max_length=500, null=True, blank=True)
    seeKeywords = models.CharField(max_length=500, null=True, blank=True)
    urlLink = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return '{} - {} - {}'.format(self.company, self.title, self.location)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {} {}'.format(self.title, self.location, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.title, self.location, self.uniqueId))
        self.seeKeywords = 'Opus, Online job application, full time jobs, part time jobs, get a job, apply for a job, {}, {}'.format(self.company.title, self.title)
        self.seeDescription = '{}'.format('Opus {} Job application, Apply for job: {} in {}, online today'.format(self.company.title, self.title, self.location))
        super(Jobs, self).save(*args, **kwargs)