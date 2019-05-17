from django.forms import ModelForm
from .models import Package
from django import forms
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class DeliveryRegForm(ModelForm):
    class Meta:
        model = Package
        fields = ['from_address', 'to_address', 'delivery_date', 'size', 'description', 'type', 'from_phone',
                  'to_phone', 'pk_user']
        widgets = {
            'delivery_date': DateInput(),
            'pk_user': forms.HiddenInput()
        }


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

"""
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    email = forms.EmailField(label="email")
    username = forms.CharField(min_length=4, label="username")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label="password")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
"""


class AuthForm(forms.Form):
    """
    class    Meta:
        model = User
        fields = ('username', 'password')
    """
    username = forms.CharField(widget=forms.TextInput, label="username")
    password = forms.CharField(widget=forms.PasswordInput, label='password')

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class EditUserForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    widgets = {

    }

    """
    username = forms.CharField(widget=forms.TextInput, label='username')
    email = forms.CharField(widget=forms.EmailField, label='email')
    first_name = forms.CharField(widget=forms.TextInput, label='first_name')
    last_name = forms.CharField(widget=forms.TextInput, label='last_name')
    """