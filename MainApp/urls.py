from django.contrib import admin
from django.urls import path
from jobs import views as jobs_views
from users import views as users_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs_views.home, name="home_page" ),
    path('register/',users_views.register, name="register" ),
    path('profile/', users_views.profile, name='profile'),
    path('jobs/', jobs_views.job_list, name='job-list'),
    path('jobs/<slug:slug>/', jobs_views.job_detail, name='job-detail'),
    path('jobs/category/<slug:slug>/', jobs_views.category_detail, name='category-detail'),
    path('users/create', users_views.create_resume, name='create-resume'),
    path('users/createjob', jobs_views.create_job, name='create-job'),
    path('users/view/<slug:slug>/', users_views.resume_detail, name='resume-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('terms-and-conditions/', jobs_views.terms, name='terms'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
