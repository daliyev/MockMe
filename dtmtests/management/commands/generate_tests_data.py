from django.core.management.base import BaseCommand
from dtmtests.models import Subject, SubjectQuestion, QuestionOption, SpecialSubject, SpecialSubjectQuestion, SpecialQuestionOption
import random


class Command(BaseCommand):
    help = 'Generates 100 subjects, each with 5 questions, and each question with 4 options.'

    def handle(self, *args, **kwargs):
        # Create 100 subjects
        subjects = Subject.objects.all()

        # Create 5 questions for each subject
        options = ['A', 'B', 'C', 'D']
        for subject in subjects:
            for question_no in range(1, 101):
                question_text = f'This is a sample question number {question_no} for {subject.name}.'
                question = SubjectQuestion.objects.create(subject_code=subject, question_no=question_no,
                                                          text=question_text)

                # Create 4 options for each question
                correct_option = random.choice(options)
                for option in options:
                    is_answer = option == correct_option
                    option_text = f'Sample answer {option} for question {question_no} of subject {subject.name}.'
                    QuestionOption.objects.create(question_no=question, is_answer=is_answer, text=option_text)

        self.stdout.write(self.style.SUCCESS('Successfully created 100 subjects with questions and options.'))
