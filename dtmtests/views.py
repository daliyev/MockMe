from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import dtmtests, SpecialSubjectTest, SubjectTest, SubjectQuestion, SpecialSubjectQuestion, StudentTest, DtmDirection
from .serializers import DtmtestsSerializer, SpecialSubjectTestSerializer, SubjectTestSerializer, SubjectQuestionSerializer, SpecialSubjectQuestionSerializer, QuestionOptionSerializer, SpecialQuestionOptionSerializer, StudentTestSerializer, DtmDirectionSerializer
from rest_framework import status


class DtmTestDetailView(RetrieveAPIView):
    queryset = dtmtests.objects.all()
    serializer_class = DtmtestsSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        sp_subject_test_data = []
        for test_code in serializer.data['sp_subjeccttest']:
            # print(test_code)
            subject_test = SpecialSubjectTest.objects.get(test_code=test_code)
            questions = subject_test.questions.all()
            for question in questions:
                options = question.special_options.all()
                question = SpecialSubjectQuestionSerializer(question).data
                # print("question", question)
                options_data = []
                for option in options:
                    question_options = SpecialQuestionOptionSerializer(option).data
                    # print("question_options", question_options)
                    options_data.append(question_options)
                sp_subject_test_data.append({
                    "special_question": question,
                    "options": options_data,
                })

        subject_test_data = []
        for test_code in serializer.data['subjecttest']:
            # print(test_code)
            subject_test = SubjectTest.objects.get(test_code=test_code)
            questions = subject_test.questions.all()
            for question in questions:
                options = question.options.all()
                question = SubjectQuestionSerializer(question).data
                # print("question", question)
                options_data = []
                for option in options:
                    question_options = QuestionOptionSerializer(option).data
                    # print("question_options", question_options)
                    options_data.append(question_options)
                subject_test_data.append({
                    "question": question,
                    "options": options_data,
                })

        # print("subject_test_data", subject_test_data)

        ctx = {
            "test": serializer.data,
            "special_tests": sp_subject_test_data,
            "subject_tests": subject_test_data
        }
        return Response(ctx, status=status.HTTP_200_OK)


class DtmTestListView(ListAPIView):
    # queryset = dtmtests.objects.all()
    serializer_class = DtmtestsSerializer

    def get_queryset(self):
        d_code = self.kwargs['direction_code']
        return dtmtests.objects.filter(direction_code=d_code)


class DtmDirectionListView(ListAPIView):
    queryset = DtmDirection.objects.all()
    serializer_class = DtmDirectionSerializer


class StudentTestResultListView(ListAPIView):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return StudentTest.objects.filter(student_id=user_id)


class StudentTestResult(CreateAPIView):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializer
