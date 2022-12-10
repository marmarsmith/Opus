from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User


from .forms import *

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    form = SearchForm()

    context = {}

    #jobs filtering
    context['meta'] = Jobs.objects.filter(company__title="Meta")[:5]
    context['sony'] = Jobs.objects.filter(company__title="Sony")[:5]
    context['apple'] = Jobs.objects.filter(company__title="Apple")[:5]
    context['google'] = Jobs.objects.filter(company__title="Google")[:5]
    context['activision'] = Jobs.objects.filter(company__title="Activision")[:5]
    context['ubisoft'] = Jobs.objects.filter(company__title="Ubisoft")[:5]
    context['ea'] = Jobs.objects.filter(company__title="EA")[:5]
    context['dell'] = Jobs.objects.filter(company__title="Dell")[:5]
    context['microsoft'] = Jobs.objects.filter(company__title="Microsoft")[:5]


    #category filtering
    context['technology'] = Category.objects.get(title='Technology')
    context['economy'] = Category.objects.get(title='Economy')
    context['hospitality'] = Category.objects.get(title='Hospitality')
    context['education'] = Category.objects.get(title='Education')
    context['marketing'] = Category.objects.get(title='Marketing')
    context['health_care'] = Category.objects.get(title='Health Care')
    context['construction'] = Category.objects.get(title='Construction')
    context['food_and_beverage'] = Category.objects.get(title='Food and Beverage')

    context['form'] = form


    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            search = form.cleaned_data.get('title')

            jobs = []
            if len(search.split())>1:
                search_list = search.split()
                item_list = []
                for item in search_list:
                    a_list = Jobs.objects.filter(title__icontains=item)
                    for x in a_list:
                        item_list.append(x)
                    [jobs.append(x) for x in item_list if x not in jobs]

                    return render(request, 'job-list.html', {'jobs': jobs})
            else:

                jobs = Jobs.objects.filter(title__icontains=search)

                return render(request, 'job-list.html', {'jobs': jobs})

        else:
            messages.error(request, 'Error Processing Your Request')
            context['form'] = form
            return render(request, 'home.html', context)

    return render(request, 'home.html',  context,)

def terms(request):
    return render(request, 'terms-and-conditions.html', {})

def job_list(request):
    job_list = Jobs.objects.all()
    job_list = job_list[:20]

    return render(request, 'job-list.html', {'jobs': job_list})

def job_detail(request, slug):
    the_job = Jobs.objects.get(slug=slug)

    return render(request, 'job-detail.html', {'object': the_job})

def category_detail(request, slug):
    the_category = Category.objects.get(slug=slug)
    context = {}

    jobs = Jobs.objects.filter(category__slug=slug)[:20]
    context['jobs'] = jobs
    context['the_category'] = the_category




    return render(request, 'category-detail.html', context)

@login_required
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj = request.user.title

            obj.save()

            messages.success(request, 'Job created Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'create-job.html', context)

    if request.method == 'GET':
        form = CreateJobForm()
        context = {'form': form}
        return render(request, 'create-job.html', context)

    return render(request, 'create-job.html', {})


