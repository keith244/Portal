from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)  
    linked_in = models.URLField(max_length=200 )
    
    def __str__(self):
            return f'{self.user.username} Profile'


class WorkExperience(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      company = models.CharField(max_length=254)
      position = models.CharField(max_length=254)
      start_date = models.DateField()
      end_date = models.DateField(blank=True, null=True)
      responsibility = models.TextField()

      def __str__(self):
            return f'{self.user.email}--{self.company}'
      
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
            return f'{self.user.email}--{self.course}'
      
      class Meta:
            verbose_name_plural = 'Education'