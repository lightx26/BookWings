from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, ChangePasswordForm, \
    UserAddressForm  # Import your registration form (if using
# one)
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.


def accountRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Use form if available
        if form.is_valid():
            user = form.save(commit=False)  # Don't save just yet
            user.set_password(form.cleaned_data['password'])  # Set password securely
            user.save()
            login(request, user)  # Log in the newly registered user
            return redirect('home')  # Redirect to your desired page after registration
    else:
        form = UserRegistrationForm()  # Create an empty form for GET requests
    context = {'form': form}
    return render(request, 'register.html', context)


class UserLoginView(LoginView):
    template_name = 'login.html'  # Your login template
    redirect_authenticated_user = True  # Redirect authenticated users to another page
    # You can also override the form_class attribute to use a custom login form
    # form_class = UserLoginForm
    # Or override the authentication_form attribute to use a custom authentication form
    authentication_form = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('home')  # Redirect to your desired page after login


def accountLogout(request):
    logout(request)
    return redirect('home')


def accountChangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            if user.check_password(form.cleaned_data['old_password']):
                user.set_password(form.cleaned_data['new_password'])
                user.save()  # Save the new password to database
                update_session_auth_hash(request, user)  # Prevent user from being logged out
                return redirect('home')
    else:
        form = ChangePasswordForm()

    context = {'form': form}
    return render(request, 'change_password.html', context)


# def accountProfile(request):
#     return render(request, 'profile.html')


def accountUpdateAddress(request):
    if request.method == 'POST':
        form = UserAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('home')
    else:
        form = UserAddressForm()

    context = {'form': form}
    return render(request, 'update_address.html', context)
