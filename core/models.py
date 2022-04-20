from django.db import models
import uuid

class Alimentacao(models.Model):
  name = models.CharField(max_length=150)
  quantity = models.FloatField()
  proteins = models.FloatField()
  carbohydrates = models.FloatField()
  fat = models.FloatField()

  def __str__(self):
      return self.name

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

