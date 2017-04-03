from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 64)
    surname = models.CharField(max_length = 64)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

class Movie(models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='director')
    actors = models.ManyToManyField(Person, through = "Role")
    year = models.IntegerField()

    def __str__(self):
        return '{}: {} Reżyser:{}, Aktorzy:{}, Rok:{}'.format(self.title, self.description, self.director, self.actors, self.year)

class Role(models.Model):
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=64)

    def __str__(self):
        return '{} {}'.format(self.person, self.role)
