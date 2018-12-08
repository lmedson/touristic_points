from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from avaliations.models import Avaliation
from adresses.models import Adress


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    avaliations = models.ManyToManyField(Avaliation)
    adresses = models.ForeignKey(
        Adress, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
