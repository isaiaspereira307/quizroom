from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Room, Question, Answer

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email='test@example.com', password='testpass', username='Test User')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'Test User')
        self.assertTrue(user.check_password('testpass'))

    def test_create_superuser(self):
        user = User.objects.create_superuser(email='admin@example.com', password='adminpass', username='Admin User')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, 'admin@example.com')
        self.assertEqual(user.username, 'Admin User')
        self.assertTrue(user.check_password('adminpass'))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


User = get_user_model()

class RoomModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass', username='Test User')

    def test_create_room(self):
        room = Room.objects.create(name='Test Room', admin=self.user, description='Test Description', limit_date='2022-12-31')
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(room.name, 'Test Room')
        self.assertEqual(room.admin, self.user)
        self.assertEqual(room.description, 'Test Description')
        self.assertEqual(str(room.limit_date), '2022-12-31')


User = get_user_model()

class QuestionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass', username='Test User')
        self.room = Room.objects.create(name='Test Room', admin=self.user, description='Test Description', limit_date='2022-12-31')

    def test_create_question(self):
        question = Question.objects.create(room_id=self.room, content='Test Question', score=10)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(question.room_id, self.room)
        self.assertEqual(question.content, 'Test Question')
        self.assertEqual(question.score, 10)


User = get_user_model()

class AnswerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass', username='Test User')
        self.room = Room.objects.create(name='Test Room', admin=self.user, description='Test Description', limit_date='2022-12-31')
        self.question = Question.objects.create(room_id=self.room, content='Test Question', score=10)

    def test_create_answer(self):
        answer = Answer.objects.create(question_id=self.question, user_id=self.user, content='Test Answer', correct=True)
        self.assertEqual(Answer.objects.count(), 1)
        self.assertEqual(answer.question_id, self.question)
        self.assertEqual(answer.user_id, self.user)
        self.assertEqual(answer.content, 'Test Answer')
        self.assertTrue(answer.correct)

