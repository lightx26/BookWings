from django.shortcuts import render, redirect
from .forms import UserRegistrationForm  # Import your registration form (if using one)
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
# Create your views here.


def register(request):
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
    # authentication_form = UserLoginForm
