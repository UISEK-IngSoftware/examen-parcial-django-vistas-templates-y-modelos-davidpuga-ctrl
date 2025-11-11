from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField("Title", max_length=200)
    genre = models.CharField("Genre", max_length=100)
    director = models.CharField("Director", max_length=150)
    year = models.IntegerField("Year")
    synopsis = models.TextField("Synopsis", max_length=1000)

    class Meta:
        ordering = ['-year', 'title']
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.title} ({self.year})"
