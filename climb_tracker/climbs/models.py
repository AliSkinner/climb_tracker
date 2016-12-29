from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location)
    description = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.location.name, self.name)

class Route(models.Model):
    grade = models.CharField(max_length=255)
    area = models.ForeignKey(Area)
    description = models.TextField()
    attempts = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {} - {}".format(self.grade,
                                     self.area.location.name,
                                     self.area.name)

class Session(models.Model):
    date = models.DateTimeField()
    duration = models.DurationField()
    location = models.ForeignKey(Location)
    activity = models.CharField(max_length=255)
    achievements = models.ManyToManyField(Route)
    notes = models.TextField()

    def __str__(self):
        return "{}-{}-{}: {}".format(self.date.day,
                                     self.date.month,
                                     self.date.year,
                                     self.location.name)
