from django.db import models


class Step(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    nextsteps = models.ManyToManyField('Step', blank=True)

    def __str__(self):
        return str(self.id)
