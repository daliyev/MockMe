from django.db import models


class TestModel(models.Model):
    code = models.CharField(max_length = 25,default = "")
    question = models.TextField()
    image = models.ImageField(upload_to='tests/',blank=True, null=True)
    answerA = models.TextField()
    answerB = models.TextField()
    answerC = models.TextField()
    answerD = models.TextField()
    answer_correct = models.CharField(max_length = 1, default = "")

    class Meta:
        db_table = 'testmodel'
        verbose_name = 'Test'
        verbose_name_plural = 'Testlar'

    def __str__(self) -> str:
        return self.code
    


class TestCollectionModel(models.Model):
    CHOICES = [
        ('math', 'Matematika'),
        ('english', 'English'),
        ('russian', 'Rus tili'),
        ('chemist', 'Kimyo'),
        ('biology', 'Biologiya'),
        ('mothlang', 'Ona tili'),
        ('history', 'Tarix'),
        ('geography', 'Geografiya'),
        ('special', 'Maburiy testlar'),
        ('physics', 'Fizika'),
    ]
    code = models.CharField(max_length = 25,default = "")
    subject = models.CharField(max_length=20, choices=CHOICES)
    tests = models.ManyToManyField(TestModel,blank=True)
    is_free = models.BooleanField(default = False)

    class Meta:
        db_table = 'testcollectionmodel'
        verbose_name = "Fanlardan test"
        verbose_name_plural = "Fanlardan testlar"

    def __str__(self) -> str:
        return f'{self.subject} testcollection-{self.code}'


class DTMTestModel(models.Model):
    code = models.CharField(max_length = 25,default = "")
    testcollection = models.ManyToManyField(TestCollectionModel,blank=True)
    is_started = models.BooleanField(default = False)

    class Meta:
        db_table = 'dtmtest'
        verbose_name = "DTM test"
        verbose_name_plural = "DTM testlar"

    def __str__(self) -> str:
        return f'{self.testcollection} dtmtest-{self.code}'
