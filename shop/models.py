from django.db import models
import datetime
import os

def get_file_name(request,filename):
    
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_file)

class Category(models.Model):

    name = models.CharField(max_length=30,null=False,blank=False)
    category_image = models.ImageField(upload_to=get_file_name,null=True,blank=False)
    status = models.BooleanField(default=True,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE)  #on_delete=models.CASCADE this helps when we delete category so simulanteously products of that categories will be deleted.
    name = models.CharField(max_length=30,null=False,blank=False)
    products_images = models.ImageField(upload_to=get_file_name,null=True,blank=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    price = models.IntegerField(null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    vendor = models.CharField(max_length=50,null=False,blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.category})'


