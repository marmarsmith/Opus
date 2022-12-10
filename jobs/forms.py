from django import forms
from .models import *


class SearchForm(forms.ModelForm):
    title = forms.CharField(
            required = True,
            widget=forms.TextInput(attrs={'class': 'form-control rounded registration-input-box', 'placeholder': 'Enter a Job Title: '}),
    )


    class Meta:
        model = Jobs
        fields = ['title']



class CreateJobForm(forms.ModelForm):
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

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Job title'})
    )

    location = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'City,ST'})
    )

    salary = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Ex: 20,000-30,000'})
    )

    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'nice-select rounded'}),
    )

    experience = forms.ChoiceField(
        choices=EXP_CHOICES,
        widget=forms.Select(attrs={'class': 'nice-select rounded'})
    )

    summary = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Job Summary'})
    )

    description = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Job Description'})
    )

    requirements = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Job Requirements'})
    )

    duties = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Duites Expected'})
    )

    owner = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Duites Expected'})
    )

    class Meta:
        model = Jobs
        fields = [
            'title',
            'location',
            'salary',
            'type',
            'experience',
            'summary',
            'description',
            'requirements',
            'duties',
            'owner',
        ]
