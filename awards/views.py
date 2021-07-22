from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects,Comments,Ratings
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.contrib.auth import logout
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .forms import CommentForm, ProfileUpdateForm, SignUpForm, NewProjectForm, UserUpdateForm

# Create your views here.
@login_required(login_url = '/accounts/login/')
def index(request):

    all_projects = Projects.all_projects()

    return render(request,'index.html',{'all_projects':all_projects})

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f'Your account has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('index')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }

    return render(request, 'update_profile.html', context)



@login_required(login_url='/accounts/login/')
def new_project(request):
    '''
    Function that will upload a new project
    '''
    if request.method=='POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            return redirect('index')

    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{'form':form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    '''
    View function to search for a project
    '''
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Projects.search_project(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{'message':message,'project':searched_projects})

    else:
        message = 'You have not entered anything to search'
        return render(request,'search.html',{'message':message})


@login_required(login_url='/accounts/login/')
def comment(request,id):
    '''
    Function to comment on a project
    '''
    id = id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            project = Projects.objects.get(id = id)
            comment.project_id = project
            comment.save()
            return redirect('index')

        else:
            project_id = id
            messages.info(request,'Ensure you fill all the fields')
            return redirect('comment',id = project_id)

    else:
        id = id
        form = CommentForm()
        return render(request,'comment.html',{'form':form,'id':id})
    


@login_required(login_url='/accounts/login/')
def single_project(request,id):
    '''
    Function for getting just a single post
    Args:id The id of the post
    '''
    project = Projects.objects.get(id = id)
    comments = Comments.objects.filter(project_id = id)
    rates = Ratings.objects.filter(project_id = id)
    designrate = []
    usabilityrate = []
    contentrate = []
    if rates:
        for rate in rates:
            designrate.append(rate.design)
            usabilityrate.append(rate.usability)
            contentrate.append(rate.content)

        total = len(designrate)*10
        design = round(sum(designrate)/total*100,1)
        usability = round(sum(usabilityrate)/total*100,1)
        content = round(sum(contentrate)/total*100,1)
        return render(request,'single_project.html',{'project':project,'comments':comments,'design':design,'usability':usability,'content':usability})

    else:
        design = 0
        usability = 0
        content = 0       

        return render(request,'single_project.html',{'project':project,'comments':comments,'design':design,'usability':usability,'content':usability})

@login_required(login_url='/accounts/login/')
def rate(request,id):
    if request.method =='POST':
        rates = Ratings.objects.filter(id = id)
        for rate in rates:
            if rate.user == request.user:
                messages.info(request,'You cannot rate a project twice')
                return redirect('singleproject',id)
        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')

        if design and usability and content:
            project = Projects.objects.get(id = id)
            rate = Ratings(design = design,usability = usability,content = content,project_id = project,user = request.user)
            rate.save()
            return redirect('singleproject',id)

        else:
            messages.info(request,'Input all fields')
            return redirect('singleproject',id)


    else:
        messages.info(request,'Input all fields')
        return redirect('singleproject',id)

@login_required(login_url="/accounts/login/")
def logout_request(request):
    '''
    Function to log out user
    '''

    logout(request)
    return redirect('index')

class ProfileList(APIView):
    def get(self,request,format = None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many = True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self,request,format = None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects,many = True)
        return Response(serializers.data)

    
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)