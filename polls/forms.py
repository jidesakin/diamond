from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )

    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32
    )

    first_name = forms.CharField(
        required = True,
        label = "First name",
        max_length = 255
    )

    last_name = forms.CharField(
        required = True,
        label = "Last name",
        max_length = 255
    )

    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

