from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model): #class=define objeto, Post=nombre de modelo
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE) #relación con otro modelo
    title = models.CharField(max_length = 200) #texto con límite
    text = models.TextField() #texto sin límite
    created_date = models.DateTimeField( #fecha y hora
        default = timezone.now)
    published_date = models.DateTimeField(
        blank = True, null= True)

    def publish(self): #def=función, publish = nombre método
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title
