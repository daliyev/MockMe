from rest_framework import serializers

from .models import dtmtests, SpecialSubjectTest, SubjectTest, SubjectQuestion, SpecialSubjectQuestion, QuestionOption, SpecialQuestionOption, StudentTest, DtmDirection
# from .views import StudentTestResult


# class DtmtestsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = dtmtests
#         fields = ['dtmtest_code', 'name', 'sp_subjeccttest', 'subjecttest']

class DtmtestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = dtmtests
        fields = '__all__'


class SpecialSubjectTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialSubjectTest
        fields = '__all__'


class SubjectTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTest
        fields = '__all__'

class SubjectQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectQuestion
        fields = '__all__'


class SpecialSubjectQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialSubjectQuestion
        fields = '__all__'


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = '__all__'


class SpecialQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialQuestionOption
        fields = '__all__'


class StudentTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = ['student_id', 'test_code', 'point', 'date']


class DtmDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtmDirection
        fields = '__all__'