from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Signature


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=10, required=True, help_text="Required.")
    aadhaar = forms.CharField(max_length=14, required=True, help_text="Required.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'aadhaar', 'password1', 'password2',)


class SignatureForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True, help_text='Required.')
    addressedTo = forms.CharField(max_length=100, required=True, help_text='Required.')

    class Meta:
        model = Signature
        fields = ('Subject', 'AddressedTo')

    @staticmethod
    def save(details, hashText):
        s = Signature(email=details["email"],
                      addressedTo=details["addressedTo"],
                      subject=details["subject"],
                      hash=hashText)
        s.save()
