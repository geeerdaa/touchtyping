from datetime import datetime
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from tasks.models import Score, Task, Achievement
from tasks.views import Leaderboards

User = get_user_model()


class TaskMenuViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy("task_menu")

    def test_get_task_menu(self):
        """
        Test that the task menu page is rendered with a list of task difficulties.
        """
        user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_login(user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_menu.html")


class TaskViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.difficulty = 0
        self.url = reverse_lazy("task", args=[self.difficulty])

    def test_get_task(self):
        """
        Test that the task page for the specified difficulty is rendered.
        """
        user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_login(user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task.html")
        # Add more assertions for the task page


class LeaderboardsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.difficulty = 0
        self.url = reverse_lazy("leaderboards", args=[self.difficulty])

    def test_post(self):
        """
        Test that a score is successfully submitted and user achievements are updated.
        """
        user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_login(user)

        # Add necessary data for the POST request
        data = {
            "time": 10
            # Add other required fields
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("home"))
        # Add assertions for updated user achievements

    # def test_get_queryset(self):
    #     """
    #     Test that the correct queryset of scores is returned for the specific task difficulty.
    #     """
    #     # Create scores for the specified task difficulty
    #
    #     response = self.client.get(self.url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "leaderboards.html")
    #     # Add assertions for the returned queryset

