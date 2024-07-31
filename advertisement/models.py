from django.db import models

class AdvertisementModel(models.Model):
    image = models.ImageField(upload_to='advertisement/')
    url = models.URLField(default = "")

    class Meta:
        db_table = 'advertisementmodel'
        verbose_name = "Reklama"
        verbose_name_plural = "Reklamalar"

    def __str__(self) -> str:
        return self.url