from django.db import models


class category(models.Model):
    name =models.CharField(max_length=30)

    @staticmethod    #decorator 
    def get_all_categories():
        return category.objects.all()
        

    def __str__(self):
        return self.name
