from django.db import models
class Register_model(models.Model):
    uid = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    branch = models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    image=models.ImageField(upload_to='stud_image',default="")

    def __str__(self):
        return self.uid











