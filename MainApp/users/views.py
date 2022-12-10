from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime


import os
from uuid import uuid4
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created successfully for user: ' + user + 'Please login now :)')
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)


    return render(request, 'register.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html', {})

@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.user = request.user

            obj.save()

            messages.success(request, 'Resume created Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'create-resume.html', context)

    if request.method == 'GET':
        form = ResumeForm()
        context = {'form': form}
        return render(request, 'create-resume.html', context)

    return render(request, 'create-resume.html', {})

class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume-detail.html'

def resume_detail(request, slug):
    obj = Resume.objects.get(slug=slug)

    educations = Education.objects.filter(resume=obj)
    experiences = Experience.objects.filter(resume=obj)
    context = {}
    context['object'] = obj
    context['educations'] = educations
    context['experiences'] = experiences

    if request.method == 'POST':
        edu_form = EducationForm(request.POST)
        if edu_form.is_valid():
            o = edu_form.save(commit=False)

            o.resume = obj
            o.save()

            messages.success(request, 'Resume Updated Successfully')
            return redirect('resume-detail', slug=slug)
        else:
            messages.error(request, 'Error Processing Your Request')
            context['edu_form'] = edu_form
            return render(request, 'resume-detail.html', context)

        if request.method == 'GET':
            edu_form = EducationForm()
            context['edu_form'] = edu_form
            return render(request, 'resume-detail.html', context)

    if request.method == 'POST':
        exp_form = ExperienceForm(request.POST)
        if exp_form.is_valid():
            o = exp_form.save(commit=False)

            o.resume = obj
            o.save()

            messages.success(request, 'Resume Updated Successfully')
            return redirect('resume-detail', slug=slug)
        else:
            messages.error(request, 'Error Processing Your Request')
            context['exp_form'] = exp_form
            return render(request, 'resume-detail.html', context)

        if request.method == 'GET':
            exp_form = ExperienceForm()
            context['exp_form'] = exp_form
            return render(request, 'resume-detail.html', context)

    return render(request, 'resume-detail.html', context)

@login_required
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.job = request.title

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