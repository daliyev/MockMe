from django.db import models
from accounts.models import AccountsModel as Student


class Subject(models.Model):
    subject_code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

    def __str__(self):
        return self.name


class SpecialSubject(models.Model):
    subject_code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Majburiy Fan"
        verbose_name_plural = "Majburiy Fanlar"

    def __str__(self):
        return self.name


class SubjectQuestion(models.Model):
    subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    question_no = models.PositiveIntegerField()
    text = models.TextField()

    class Meta:
        verbose_name = "Test savol"
        verbose_name_plural = "Test savollari"

    def __str__(self):
        return f"{self.subject_code} - {self.question_no}"


class QuestionOption(models.Model):
    question_no = models.ForeignKey(SubjectQuestion, on_delete=models.CASCADE, related_name='options')
    is_answer = models.BooleanField(default=False)
    text = models.TextField()

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Javob variantlari"

    def __str__(self):
        return f"Question {self.id} "


class SpecialSubjectQuestion(models.Model):
    subject_code = models.ForeignKey(SpecialSubject, on_delete=models.CASCADE, related_name='special_questions')
    question_no = models.PositiveIntegerField()
    text = models.TextField()

    class Meta:
        verbose_name = "Test savol"
        verbose_name_plural = "Majburiy Test savollari"

    def __str__(self):
        return f"{self.subject_code} - {self.question_no}"


class SpecialQuestionOption(models.Model):
    question_no = models.ForeignKey(SpecialSubjectQuestion, on_delete=models.CASCADE, related_name='special_options')
    is_answer = models.BooleanField(default=False)
    text = models.TextField()

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Majburiy Javob variantlari"

    def __str__(self):
        return f"Question {self.question_no} "


class SubjectTest(models.Model):
    subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_code = models.CharField(max_length=20, primary_key=True)
    questions = models.ManyToManyField(SubjectQuestion, blank=True, related_name='subject_question')

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Yo'nalish test"

    def __str__(self):
        return f'{str(self.test_code)}-{self.subject_code}'


class SpecialSubjectTest(models.Model):
    subject_code = models.ForeignKey(SpecialSubject, on_delete=models.CASCADE)
    test_code = models.CharField(max_length=20, primary_key=True)
    questions = models.ManyToManyField(SpecialSubjectQuestion, blank=True)

    class Meta:
        verbose_name = "Majburiy Test"
        verbose_name_plural = "Majburiy Yo'nalish test"

    def __str__(self):
        return f'{str(self.test_code)}-{self.subject_code}'


class DtmDirection(models.Model):
    # direction_code = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dtm yo'nalish"
        verbose_name_plural = "Dtm yo'nalishlar"

    def __str__(self):
        return self.name


class dtmtests(models.Model):
    direction_code = models.ForeignKey(DtmDirection, on_delete=models.CASCADE, related_name='tests', null=True)
    dtmtest_code = models.CharField(max_length=20, primary_key=True)
    # name = models.CharField(max_length=100)
    sp_subjeccttest = models.ManyToManyField(SpecialSubjectTest, related_name='sp_subjecttest')
    subjecttest = models.ManyToManyField(SubjectTest, related_name='subjecttest')

    class Meta:
        verbose_name = "DTM test"
        verbose_name_plural = "DTM testlar blok"

    def __str__(self):
        return f'{self.direction_code.name} {str(self.dtmtest_code)}'


class StudentTest(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    test_code = models.ForeignKey(dtmtests, on_delete=models.CASCADE, related_name='dtmtest')
    point = models.FloatField(default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.student_id} - {self.test_code} on {self.date}"


# class StudentResponse(models.Model):
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     test_code = models.ForeignKey(SubjectTest, on_delete=models.CASCADE)
#     question_no = models.ForeignKey(SubjectQuestion, on_delete=models.CASCADE)
#     option_no = models.ForeignKey(QuestionOption, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('student_id', 'subject_code', 'test_code', 'question_no', 'option_no')
#
#     def __str__(self):
#         return f"{self.student_id} - {self.test_code} - {self.question_no} - {self.option_no}"
