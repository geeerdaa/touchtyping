# from django import forms
# from accounts.models import UserProfile
#
#
# class UserProfileSignupForm(forms.ModelForm):
#     avatar = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={'class': 'ask-signup-avatar-input', }),
#         required=False, label=u'Аватар'
#     )
#
#     def clean_avatar(self):
#         avatar = self.cleaned_data.get('avatar')
#         if avatar is None:
#             raise forms.ValidationError(u'Добавьте картинку')
#         if 'image' not in avatar.content_type:
#             raise forms.ValidationError(u'Неверный формат картинки')
#         return avatar
#
#     class Meta:
#         model = UserProfile
#         fields = ('avatar')
