# Generated by Django 4.0.3 on 2022-05-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_category_company_remove_jobs_logo_jobs_applications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='experience',
            field=models.CharField(choices=[('Less than 2yrs', 'Less than 2yrs'), ('2yrs - 5yrs', '2yrs - 5yrs'), ('5yrs - 10 yrs', '5yrs - 10 yrs'), ('10yrs - 15yrs', '10yrs - 15yrs'), ('More than 15yrs', 'More than 15yrs'), ('Not Provided', 'NP')], default='Not Provided', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type',
            field=models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('Not Provided', 'N/A'), ('RT', 'Remote')], default='Not Provided', max_length=100),
        ),
    ]
