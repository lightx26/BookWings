from django import forms
from .models import User, Address


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'password', 'first_name', 'last_name']


# class UserLoginForm(AdminAuthenticationForm):
#     username = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={'maxlength': 150}),
#     )


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')
        if new_password != confirm_new_password:
            raise forms.ValidationError('Passwords do not match')


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['local_address', 'commune', 'district', 'province']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
