from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=50,verbose_name="Title OF Post") #verboseName:appears on our form the same as here
    #if we dont mention the verbose name , title,description or is_active appears on our form ! 
    description=models.CharField(max_length=300,verbose_name="Description")
    is_active=models.BooleanField(default=False,verbose_name="Status")
    
    def __str__(self):
        return self.title+" "+self.description +" " +str(self.is_active)







 





