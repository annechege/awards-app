from django.conf.urls import url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.index, name='index'),
    path('profile/',views.profile,name = 'profile'),
    url(r'^newproject/$',views.new_project,name='newproject'),
    url(r'^search/',views.search_results,name = 'search_results'),
    path('comment/<int:id>/',views.comment,name='comment'),
    url(r'^update_profile/$',views.update_profile,name='update_profile'),
    url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
    path('rate/<int:id>/',views.rate,name='rates'),
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/projects/$',views.ProjectList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)