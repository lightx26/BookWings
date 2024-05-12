from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, ChangePasswordForm, \
    UserAddressForm  # Import your registration form (if using
# one)
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from cart.models import Cart

import accounts.services as accounts_services


# Create your views here.
def accountRegister(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Use form if available
        if form.is_valid():
            user = form.save(commit=False)  # Don't save just yet
            user.set_password(form.cleaned_data['password'])  # Set password securely
            user.save()

            cart = Cart(customer=user)
            cart.save()

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


@login_required
def log_out(request):
    logout(request)
    return redirect('home')


@login_required
def change_password(request):
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


@login_required
def update_address(request):
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


@login_required
def remove_address(request):
    if request.method == 'POST':
        address_ids = request.POST.getlist('addresses[]')
        for address_id in address_ids:
            address = accounts_services.get_address_by_id(address_id)
            address.delete()

        return redirect('home')

    addresses = accounts_services.get_addresses_by_user(request.user)
    return render(request, 'remove_address.html', {'addresses': addresses})


# TODO: View profile
@login_required
def view_profile(request):
    return render(request, 'profile.html')
