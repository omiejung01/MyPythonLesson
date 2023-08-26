from django import forms


class RegisterForm(forms.Form):
    fullname = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your full name',
               }),required=True)

    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your username',
               }),required=True)

    email = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your email',
               }),required=True)

    phone = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your number',
               }),required=True)

    password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your password',
               'onkeyup': 'verify_password()'
               }),required=True)

    confirm_password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm your password',
               'onkeyup': 'verify_password()'
               }),required=True)


class LoginForm(forms.Form):
    email = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your email',
               }),required=True)
    password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your password',
               }),required=True)