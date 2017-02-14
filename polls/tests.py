from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        future_time = timezone.now()+datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertEqual(future_question.was_published_resently(), False)