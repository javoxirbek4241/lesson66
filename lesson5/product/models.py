from django.db import models

class Apartments(models.Model):
    title = models.CharField(max_length=25)
    desc = models.TextField()
    address = models.TextField()
    rooms = models.IntegerField()
    image = models.ImageField(upload_to = 'apartments/', default='default/house.png')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='$')

    def __str__(self):
        return self.title
