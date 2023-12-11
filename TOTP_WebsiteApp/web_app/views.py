from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views import View
from .forms import CustomUserCreationForm, AddAccountForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from .utils import send_sms
from django.http import JsonResponse

# Model to create a new user
class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm  # Use the updated form with the 'phone_number' field
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Get the phone number from the form
        phone_number = form.cleaned_data.get('phone_number')

        # Create a UserProfile for the user and associate it
        user_profile, created = UserProfile.objects.get_or_create(user=self.object)
        user_profile.phone_number = phone_number
        user_profile.save()

        # Send an SMS after successful signup
        message = "Welcome to my Password Manager app! Thanks for signing up. We will take great care in managing your passwords. >:)"
        send_sms(phone_number, message)

        # Log the user in after signup
        login(self.request, self.object)

        return response

class CustomLoginView(LoginView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Fetch the logged-in user
        user = self.request.user

        # Try to get the associated phone number based on user_id
        try:
            user_profile = UserProfile.objects.get(user_id=user.id)
            user_phone_number = user_profile.phone_number
        except UserProfile.DoesNotExist:
            user_phone_number = None

        # Check if a phone number exists for the user and send an SMS alert
        if user_phone_number:
            message = "Someone has signed into your account. If this was not you, please contact support immediately."
            send_sms(user_phone_number, message)

        return response


@method_decorator(login_required, name='dispatch')
class AccountInfoView(LoginRequiredMixin, View):
    template_name = 'registration/account_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the user's information
        user = self.request.user
        context['user'] = user
        # Add any additional context data you need for the account_info.html template
        return context
    
class AddAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/add_account.html'

    def get(self, request):
        form = AddAccountForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddAccountForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            password_entry.save()
            # Redirect to a relevant page after adding an account
            return redirect(reverse('account_info'))  # Use the name of the URL pattern
        return render(request, self.template_name, {'form': form})


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
