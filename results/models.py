from datetime import datetime
from django.db import models
from dtmtest.models import TestCollectionModel
from accounts.models import AccountsModel


class ResultsModel(models.Model):
    user_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE, default=None)
    test_id = models.ForeignKey(TestCollectionModel, on_delete=models.CASCADE)
    point = models.FloatField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "result"
        verbose_name_plural = "results"


    def __str__(self) -> str:
        return str(self.id)