from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView, ListView, DeleteView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views import View
from .forms import CustomUserCreationForm, AddAccountForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile, PasswordEntry
from .utils import send_sms
from django.http import JsonResponse

# Model to create a new user
class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm  # Use the updated form with the 'phone_number' field
    success_url = reverse_lazy('profile')
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

# Thie Custom View retrieves the phone number from the user's profile and sends an SMS after successful login

class CustomLoginView(LoginView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('registration/profile.html')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the phone number from the user's profile
        phone_number = None
        if self.request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=self.request.user)
                phone_number = user_profile.phone_number
                message = "You have logged in to your account. If this wasn't you, please contact us immediately."
                send_sms(phone_number, message)
            except UserProfile.DoesNotExist:
                pass
        context['phone_number'] = phone_number
        return context



@method_decorator(login_required, name='dispatch')
class AccountInfoView(LoginRequiredMixin, View):
    template_name = 'registration/account_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve the user's information
        user = self.request.user
        context['user'] = user
        
        # Retrieve password entries for the user
        password_entries = PasswordEntry.objects.filter(user=user)
        context['password_entries'] = password_entries
        
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
            return redirect(reverse('view_account'))  # Use the name of the URL pattern
        return render(request, self.template_name, {'form': form})


class PasswordEntryDetailView(DetailView):
    model = PasswordEntry  # Specify the model
    template_name = 'registration/passwordentry_detail.html'  # Create a new template for displaying details
    context_object_name = 'password_entry'  # Define the context variable name
    
class ViewAccountView(LoginRequiredMixin, ListView):
    model = PasswordEntry
    template_name = 'registration/view_account.html'
    context_object_name = 'password_entries'

    def get_queryset(self):
        # Override the queryset to return only entries for the current user
        return PasswordEntry.objects.filter(user=self.request.user)


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
