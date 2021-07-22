from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/', blank = 'true', default = 'default.png')
    bio = models.TextField(max_length=300)
    date_created= models.DateField(auto_now_add=True )


    def __str__(self):
        return  f'{self.user.username} Profile'

    def save_profile(self):
        '''
        Function to save a user profile
        '''
        self.save()

    def delete_profile(self):
        '''
        Function to delete a user profile
        '''
        self.delete()
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)

class Projects(models.Model):
    '''
    Class for instantiating all projects objects
    '''
    title = models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    link=models.URLField()
    image=models.ImageField(upload_to='pictures/')
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    

    def save_project(self):
        '''
        Function for saving a project
        '''
        self.save()

    @classmethod
    def all_projects(cls):
        '''
        Function for getting all projects
        '''
        all_projects = cls.objects.all()
        return all_projects

    @classmethod
    def one_project(cls,id):
        '''
        Function to get only one project.

        Args:
        id: The id of the project
        '''
        one_project = cls.objects.filter(id=id)
        return one_project

    @classmethod
    def user_projects(cls,user):
        '''
        Function for getting all projects of a particular user
        Args:
        user:Current active user
        '''
        user_projects = cls.objects.filter(user = user)
        return user_projects

    @classmethod
    def search_project(cls,search_term):
        '''
        Function for searching project by name
        '''
        searched_project = cls.objects.filter(title = search_term)
        return searched_project

class Comments(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.user

    @classmethod
    def get_all_comments(cls,id):
        ''''
        Function for getting all comments
        '''
        comments = cls.objects.filter(project_id = id)
        return comments

    def save_comments(self):
        '''
        Function for saving posted comments
        '''
        self.save()

    def delete_comment(self):
        '''
        Function for deleting a comment
        '''
        self.delete()

class Ratings(models.Model):
    design = models.IntegerField(default=1)
    usability = models.IntegerField(default=1)
    content = models.IntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)