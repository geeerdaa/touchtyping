from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

# Create your forms here.


class NewUserForm(UserCreationForm):
    """
    Form for creating a new user.

    This form extends Django's UserCreationForm to include an additional 'email' field.
    It is used for creating a new user in the system.

    Attributes:
        email (forms.EmailField): Email field for the user.

    Meta:
        model (User): The model associated with the form.
        fields (tuple): The fields to be included in the form.

    Methods:
        save(commit=True): Saves the new user instance.

    Usage:
        - Instantiate the form in a view and render it in a template to allow user registration.
        - Call the `save` method to save the new user instance.

    Example:
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic or redirect after successful user creation
        else:
            # Handle form errors or invalid submissions
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        """
        Save the new user instance.

        Args:
            commit (bool): Whether to save the user instance to the database.

        Returns:
            User: The saved user instance.

        Usage:
            user = form.save()
        """
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
