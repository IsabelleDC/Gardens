from django.contrib.auth.forms import UserCreationForm
from django import forms
from gardens_app.models import Visitor


class VisitorCreationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Visitor.objects.get(username=username)
        except Visitor.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    class Meta:
        model = Visitor
        fields = ('username', 'email', 'password1', 'password2')