from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.core.validators import RegexValidator

User = get_user_model()

# Create your models here.
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
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      education  = models.CharField(max_length=255)
      course  = models.CharField(max_length=255)
      institution  = models.CharField(max_length=255)
      grad_year = models.DateField(blank=True, null=True)
      addn_courses = models.CharField(max_length=255, blank=True, null=True)

      def __str__(self) :
            return f'{self.course}--{self.user.name}'
      
      class Meta:
            verbose_name_plural = 'Education'


class Jobs(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      title = models.CharField(max_length=255)
      responsibilities = models.TextField()
      requirements = models.TextField()
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


class Applications(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      job  = models.ForeignKey(Jobs,on_delete=models.CASCADE)
      status = models.CharField(max_length=254, blank=True, null=True)
      applied_date = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f'{self.user.name} - {self.job.title}'
      
      class Meta:
            verbose_name_plural = 'Applications'