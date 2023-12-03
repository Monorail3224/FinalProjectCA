# TOTP Website App

The TOTP Website App is a Django-based web application that allows users to securely store and manage Time-Based One-Time Passwords (TOTP) for various websites. TOTP is commonly used for two-factor authentication (2FA) to enhance the security of online accounts.

## Features

- User Registration: Create an account to get started.
- User Authentication: Log in securely using your registered credentials.
- TOTP Management: Add, view, and manage TOTP tokens for different websites.
- Account Settings: Customize your profile and security preferences.
- Password Management: Change or reset your password as needed.

## Installation

Follow these steps to install and run the TOTP Website App on your local machine:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/TOTP_WebsiteApp.git
   cd TOTP_WebsiteApp


python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate


python manage.py createsuperuser


python manage.py runserver


Usage

    Register an Account:
        Open your web browser and navigate to http://127.0.0.1:8000/.
        Click the "Register" link to create a new account.

    Log In:
        After registration, click the "Sign In" link to log in using your credentials.

    Manage TOTP Tokens:
        Once logged in, you can add, view, and manage your TOTP tokens.
        Use the "Add Website" feature to store TOTP tokens for different websites.

    Account Settings:
        Customize your profile settings and change your password in the "Account Settings" section.

    Admin Panel:
        Access the Django admin panel at http://127.0.0.1:8000/admin/ to manage users and tokens as an admin.

Contributors

    Your Name (your@email.com)
    Collaborator 1 (collaborator1@email.com)
    Collaborator 2 (collaborator2@email.com)

License

This project is licensed under the MIT License.
