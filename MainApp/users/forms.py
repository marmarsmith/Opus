from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Resume, Education, Experience

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    check = forms.BooleanField(required = True)


    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
        ]

class ResumeForm(forms.ModelForm):
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

        image = forms.ImageField(
            required=False,
            widget=forms.FileInput(attrs={'class': 'form-control'})
        )

        date_birth = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter a date: '}),
        )

        ethnicity = forms.ChoiceField(
            choices=ETHNICITY_CHOICES,
            widget=forms.Select(attrs={'class': 'nice-select rounded'}),
        )

        sex = forms.ChoiceField(
            choices = SEX_CHOICES,
            widget=forms.Select(attrs={'class': 'nice-select rounded'})
        )

        marital_status = forms.ChoiceField(
            choices = MARITAL_CHOICES,
            widget=forms.Select(attrs={'class': 'nice-select rounded'})
        )

        addressLine1 = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address 1'}),
        )

        addressLine2 = forms.CharField(
            required=False,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address 2'}),
        )

        suburb = forms.CharField(
            required=False,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Suburb'}),
        )

        city = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter City'}),
        )

        region = forms.ChoiceField(
            choices = REGION_CHOICES,
            widget=forms.Select(attrs={'class': 'nice-select rounded'}),
        )

        phoneNumber = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Phone Number'}),
        )

        cover_letter = forms.FileField(
            required=False,
            widget=forms.FileInput(attrs={'class': 'form-control'})
        )

        cv = forms.FileField(
            required=False,
            widget=forms.FileInput(attrs={'class': 'form-control'})
        )

        class Meta:
            model = Resume
            fields = [
            'image',
            'date_birth',
            'ethnicity',
            'sex',
            'marital_status',
            'addressLine1',
            'addressLine2',
            'suburb',
            'city',
            'region',
            'phoneNumber',
            'cover_letter',
            'cv'
            ]

class EducationForm(forms.ModelForm):
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

        institution = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Institution'})
        )

        qualification = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Qualification'})
        )

        level = forms.ChoiceField(
            choices=LEVEL_CHOICES,
            widget=forms.Select(attrs={'class': 'nice-select rounded'}),
        )

        start_date = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter enrollment date: '}),
        )

        graduated = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter graduation date: '}),
        )

        major_subject = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Major'})
        )

        class Meta:
            model = Education
            fields = [
            'institution',
            'qualification',
            'level',
            'start_date',
            'graduated',
            'major_subject',
            ]


class ExperienceForm(forms.ModelForm):
        company = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Company'})
        )
        position = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Position'})
        )
        start_date = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date: '}),
        )
        end_date = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End Date: '}),
        )
        experience = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Experience'})
        )
        skills = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Skills'})
        )

        class Meta:
            model = Experience
            fields = [
            'company',
            'position',
            'start_date',
            'end_date',
            'experience',
            'skills',
            ]



