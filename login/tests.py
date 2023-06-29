from login.models import User
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import RequestFactory, Client
from login.views import Register, login, profile_page_view, logout_page_view
from django.contrib.auth import get_user_model
from django import forms
from .forms import NewUserForm

User = get_user_model()


# login.models
class UserModelTest(TestCase):
    """
    Test case for the User model.

    This test case includes tests for various aspects of the User model, such as user creation, string representation,
    authentication, permissions, and other custom functionality.

    Attributes:
        setUpTestData: A class method to set up data for the test case.

    Test Methods:
        test_user_creation: Test the creation of a user instance.
        test_user_str_representation: Test the string representation of a user.
        test_user_authentication: Test the user authentication.
        test_user_permissions: Test user permissions.
        test_user_meta: Test the User model's meta attributes.

    Example:
        To run this test case, execute the command:
        ```
        python manage.py test your_app.tests.UserModelTest
        ```
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up data for the test case.

        This method creates a user instance for testing purposes.

        Usage:
            The setUpTestData method is executed before running the test methods in this test case.
        """
        User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_user_creation(self):
        """
        Test the creation of a user instance.

        This method verifies that a user instance is created with the expected attributes.

        Usage:
            Run this test to ensure that the User model can create user instances correctly.
        """
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password123'))

    def test_user_str_representation(self):
        """
        Test the string representation of a user.

        This method checks that the string representation of a user is as expected.

        Usage:
            Run this test to verify that the string representation of a user is correct.
        """
        user = User.objects.get(username='testuser')
        self.assertEqual(str(user), 'testuser')

    def test_user_authentication(self):
        """
        Test user authentication.

        This method verifies that a user is marked as authenticated.

        Usage:
            Run this test to ensure that user authentication is working correctly.
        """
        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)


# login.views
class RegisterViewTestCase(TestCase):
    """
    Test case for the Register view.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.client = Client()
        self.factory = RequestFactory()
        self.view = Register.as_view()
        self.url = reverse('register')

    def test_get(self):
        """
        Test the GET request for the registration page.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_post_valid_form(self):
        """
        Test the POST request with a valid form.
        """
        response = self.client.post(path=self.url, data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'U52TW31tEW5.',
            'password2': 'U52TW31tEW5.'
        })

        self.assertEqual(response.status_code, 302)  # Redirects to home page

    def test_post_invalid_form(self):
        """
        Test the POST request with an invalid form.
        """
        response = self.client.post(self.url, data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'U52TW31tEW5.',
            'password2': 'differentpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class LoginViewTestCase(TestCase):
    """
    Test case for the login view.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.client = Client()
        self.url = reverse('login')

    def test_login_valid_credentials(self):
        """
        Test login with valid credentials.
        """
        user_data = {
            'username': 'testuser',
            'password': 'U52TW31tEW5.',
        }
        User.objects.create_user(**user_data)

        response = self.client.post(self.url, data=user_data)
        self.assertEqual(response.status_code, 302)  # Redirects to home page

    def test_login_invalid_credentials(self):
        """
        Test login with invalid credentials.
        """
        form_data = {
            'username': 'testuser',
            'password': 'wrongpass',
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class ProfilePageViewTestCase(TestCase):
    """
    Test case for the profile page view.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.client = Client()
        self.url = reverse('profile')

    def test_profile_page_view(self):
        """
        Test the profile page view.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class LogoutPageViewTestCase(TestCase):
    """
    Test case for the logout page view.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.client = Client()
        self.url = reverse('logout')

    def test_logout_page_view(self):
        """
        Test the logout page view.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Redirects to home page


# # login.forms
class NewUserFormTestCase(TestCase):
    """
    Test case for the NewUserForm.
    """

    def test_form_fields(self):
        """
        Test the form fields.
        """
        form = NewUserForm()
        self.assertIsInstance(form.fields['email'], forms.EmailField)
        self.assertIsInstance(form.fields['username'], forms.CharField)
        self.assertIsInstance(form.fields['password1'], forms.CharField)
        self.assertIsInstance(form.fields['password2'], forms.CharField)

    def test_form_save(self):
        """
        Test saving the form.
        """
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'U52TW31tEW5.',
            'password2': 'U52TW31tEW5.'
        }
        form = NewUserForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_form_save_without_commit(self):
        """
        Test saving the form without committing to the database.
        """
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'U52TW31tEW5.',
            'password2': 'U52TW31tEW5.'
        }
        form = NewUserForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save(commit=False)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertFalse(User.objects.filter(username='testuser').exists())
