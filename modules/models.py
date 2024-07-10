from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about = models.TextField()
    job = models.CharField(max_length=150)
    #how do i create a single field called socials here that can then be extended by fields below?
    linked_in = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)


    def __str__(self):
            return f'{self.user.name} Profile'
    class Meta:
          verbose_name_plural = 'User Profile'



class WorkExperience(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      company = models.CharField(max_length=254)
      position = models.CharField(max_length=254)
      start_date = models.DateField()
      end_date = models.DateField(blank=True, null=True)
      responsibility = models.TextField()

      def __str__(self):
            return f'{self.user.name}--{self.company}'
      
      class Meta:
            verbose_name_plural = 'Work Experience'

class Education(models.Model):
      user              = models.ForeignKey(User, on_delete=models.CASCADE)
      education         = models.CharField(max_length=255)
      course            = models.CharField(max_length=255)
      institution       = models.CharField(max_length=255)
      grad_year         = models.DateField(blank=True, null=True)
      addn_courses      = models.CharField(max_length=255, blank=True, null=True)

      def __str__(self) :
            return f'{self.course}--{self.user.name}'
      
      class Meta:
            verbose_name_plural = 'Education'


class Jobs(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      title             = models.CharField(max_length=255)
      responsibilities  = models.TextField()
      requirements      = models.TextField()
      timestamp = models.DateTimeField(default=datetime.now)

      def __str__(self):
            return f'{self.title} posted by {self.user.name}'
      class Meta:
            verbose_name_plural = 'Jobs'

class Documents(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      title = models.CharField(max_length=20)
      file  = models.FileField(upload_to='documents')
      #timestamp = models.DateTimeField(default=datetime.now, auto_now_add=True)

      def __str__(self):
            return f'{self.title}--{self.user.name}'
      
      class Meta:
            verbose_name_plural = 'Documents'
      