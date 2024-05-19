from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ChangePasswordForm, UserAddressForm
from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.contrib.auth import logout
from .models import User, UserRole
from .decorators import role_required
from cart.models import Cart

import accounts.services as accounts_services

from django.http import JsonResponse


# Create your views here.
def accountRegister(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        try:
            form = UserRegistrationForm(request.POST)  # Use form if available
            if form.is_valid():
                check_user = User.objects.filter(email=form.cleaned_data['email'],
                                                 phone_number=form.cleaned_data['phone_number']).first()
                if check_user:
                    return JsonResponse({'status': "error", 'message': 'User already exists'})

                user = form.save(commit=False)  # Don't save just yet
                user.set_password(form.cleaned_data['password'])  # Set password securely
                user.save()

                cart = Cart(customer=user)
                cart.save()

                # login(request, user)  # Log in the newly registered user
                return JsonResponse(
                    {'status': "success", 'message': 'Registration successful. Please login to continue.'})
            else:
                return JsonResponse({'status': "error", 'errors': form.errors.as_json()})
        except Exception as e:
            e.with_traceback()
            return JsonResponse({'status': "error", 'message': 'Registration failed'})
    else:
        form = UserRegistrationForm()  # Create an empty form for GET requests
    context = {'form': form}
    return render(request, 'register.html', context)


# class UserLoginView(LoginView):
#     template_name = 'login.html'  # Your login template
#     redirect_authenticated_user = True  # Redirect authenticated users to another page
#     # You can also override the form_class attribute to use a custom login form
#     # form_class = UserLoginForm
#     # # Or override the authentication_form attribute to use a custom authentication form
#     authentication_form = UserLoginForm
#
#     def get_success_url(self):
#         return reverse_lazy('home')  # Redirect to your desired page after login


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username_input = request.POST['username']
        password_input = request.POST['password']
        user = authenticate(request, username=username_input, password=password_input)

        if user is not None:
            login(request, user)  # Log in the user
            # return redirect('home')  # Redirect to your desired page after login
            return JsonResponse({'status': "success", 'message': 'Login successful'})
    else:
        username_input = ''

    # return render(request, 'login.html', {'username': username_input})
    return JsonResponse({'status': "error", 'message': 'Login failed'})


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
                # return redirect('home')

                return JsonResponse({'status': "success", 'message': 'Password changed successfully'})

            else:
                return JsonResponse({'status': "error", 'message': 'Old password is incorrect'})
        else:
            return JsonResponse({'status': "error", 'errors': form.errors.as_json()})
    else:
        form = ChangePasswordForm()

    context = {'form': form}
    return render(request, 'change_password.html', context)


# def accountProfile(request):
#     return render(request, 'profile.html')


@login_required
def update_address(request):
    # if request.method == 'POST':
    #     form = UserAddressForm(request.POST)
    #     if form.is_valid():
    #         address = form.save(commit=False)
    #         address.user = request.user
    #         address.save()
    #         return redirect('home')
    # else:
    #     form = UserAddressForm()
    #
    # context = {'form': form}
    address = {}
    if request.method == 'POST':
        address['local_addr'] = request.POST.get('local_addr')
        address['commune'] = request.POST.get('commune')
        address['district'] = request.POST.get('district')
        address['province'] = request.POST.get('province')

        if accounts_services.create_address(request.user, address) is None:
            return JsonResponse({'status': "error", 'message': 'Failed to add address'})

        return JsonResponse({'status': "success", 'message': 'Address added successfully'})


@login_required
def remove_address(request, addr_id):
    if request.method == 'POST':
        address = accounts_services.get_address_by_id(addr_id)
        address.delete()

        return redirect('/accounts/profile')

    addresses = accounts_services.get_addresses_by_user(request.user)
    return render(request, 'remove_address.html', {'addresses': addresses})


@login_required
def view_addresses(request):
    addresses = accounts_services.get_addresses_by_user(request.user)
    return render(request, 'view_address.html', {'addresses': addresses})


@login_required
def view_profile(request):
    user = request.user
    address = user.address_set.all()
    print(address.count())
    return render(request, 'user/view-profile.html', {'user': user, 'addresses': address})
    # if user.role == 'customer':
    #     return view_customer_profile(request, user)
    # elif user.role == 'deliverer':
    #     return view_deliverer_profile(request, user)


@role_required([UserRole.CUSTOMER])
def view_customer_profile(request, customer):
    return render(request, 'customer_profile.html', {'customer': customer})


@role_required([UserRole.DELIVERER])
def view_deliverer_profile(request, deliverer):
    return render(request, 'deliverer_profile.html', {'deliverer': deliverer})
