from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=255)
    auteurs = models.CharField(max_length=255)
    institutions = models.CharField(max_length=255)
    resume = models.TextField()
    contenu = models.TextField()
    references = models.CharField(max_length=255)
    motsCles = models.CharField(max_length=255)
    urlPDF = models.CharField(max_length=255)
    pathPDF = models.CharField(max_length=255)
    publication_date = models.DateField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    search = models.IntegerField(default=0)

    def __str__(self):
        return self.titre
