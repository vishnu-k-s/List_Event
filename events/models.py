from django.db import models


# class Events(models.Model):

#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=100)
#     location = models.CharField(max_length=50)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     image = models.ImageField(upload_to='media')
#     published = models.BooleanField(default=False)
#     paid = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


class Categories(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to='event-images')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    published = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
    
