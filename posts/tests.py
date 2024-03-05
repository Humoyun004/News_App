from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.utils.timezone import now

from .models import News


class NewsViewTest(TestCase):
    def setUp(self):
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content")
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='password')
        self.news = News.objects.create(user=self.user,title='Test News', content='Test content', post_date=now,
                                        image=image_file)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.post('/search/', {'searched': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('news', response.context)
        self.assertTrue(News.objects.filter(title__icontains='Test'))


class UsersViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_signup(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/register/', {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_profile(self):
        self.client.force_login(self.user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('user', response.context)
        self.assertEqual(response.context['user'], self.user)




