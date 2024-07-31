
from django.core.management.base import BaseCommand
from dtmtest.models import TestModel
import random


class Command(BaseCommand):
    help = 'Generates 100 test entries in the database'

    def handle(self, *args, **kwargs):
        # Define sample answers
        answers = ['A', 'B', 'C', 'D']

        # Create 100 test entries
        for j in range(1, 101):
            for i in range(1, 101):
                code = f'Test-{i}'
                question = f'This is a sample question number {i}?'
                image = None  # Assuming you don’t have images to upload, or you can specify an image path
                answerA = f'Sample answer A for test {i}'
                answerB = f'Sample answer B for test {i}'
                answerC = f'Sample answer C for test {i}'
                answerD = f'Sample answer D for test {i}'
                answer_correct = random.choice(answers)

                TestModel.objects.create(
                    code=code,
                    question=question,
                    image=image,
                    answerA=answerA,
                    answerB=answerB,
                    answerC=answerC,
                    answerD=answerD,
                    answer_correct=answer_correct
                )

        self.stdout.write(self.style.SUCCESS('Successfully created 100 test entries.'))
