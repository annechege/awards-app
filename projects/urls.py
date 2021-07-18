from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('register/',views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('search/', views.searchprofile, name='search'),
    path('newproject/',views.addProject,name = 'project'),
    path('profile/<id>/',views.profile,name = 'profile'),
    path('editprofile/',views.editprofile,name = 'editprofile'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/profile',views.ProfileList.as_view()),
    path('api/projects',views.ProjectList.as_view()),
    path('projects/<id>/',views.projects,name = 'projects'),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    path('rate/<id>/',views.rate,name = 'rate')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)