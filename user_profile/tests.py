from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='U52TW31tEW5.')

    def test_achievements_view(self):
        """
            Test the achievements view.
        """
        self.client.login(username='testuser', password='U52TW31tEW5.')
        response = self.client.get(reverse('achievements'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'achievements.html')

    def test_stats_view(self):
        """
            Test the stats view.
        """
        self.client.login(username='testuser', password='U52TW31tEW5.')
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')

    def test_friend_view(self):
        """
            Test the friend list view.
        """
        self.client.login(username='testuser', password='U52TW31tEW5.')
        response = self.client.get(reverse('friend'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'friend.html')

    def test_profile_settings_view(self):
        """
            Test the profile settings view.
        """
        self.client.login(username='testuser', password='U52TW31tEW5.')
        response = self.client.get(reverse('profile_settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_settings.html')

    def test_user_profile_view(self):
        """
            Test the user profile view.
        """
        self.client.login(username='testuser', password='U52TW31tEW5.')
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_user_profile_view_post(self):
        """
            Test the user profile view (method POST).
        """
        self.client.login(username='testuser', password='U52TW31tEW5.')
        response = self.client.post(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
