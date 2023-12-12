# Simple Web-based Password Manager

# **IMPORTANT NOTICE**: This app is a Proof of Concept and lacks security measures. Data stored in the database is NOT encrypted.

## Overview

This is a simple web-based password manager application designed to help users store and manage their login credentials for various websites. The application provides the following core features:

- User Registration: Users can create an account by providing their email address and choosing a strong password.

- Authentication: Registered users can log in securely to access their stored passwords.

- Password Item Management: Users can create, view, edit, and delete password items for websites they frequently visit. Each password item includes fields for the website URL, username, password, and additional notes.

- Recieve SMS Notifications upon user account creation and sign-in


## Getting Started

### Prerequisites

Before you can use this application, you need to have the following installed:

- Python
- MUST have config.py file with user-defined variables in order for SMS notifications to work
### Installation

Follow these steps to set up and run the password manager application:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/password-manager.git


2. Navigate to the project directory 

    ```bash
    cd password-manager

3. Install the project dependencies

    ```bash
    pip install -r requirements.txt

4. Create the project files initial migrations
    ```bash
    python manage.py makemigrations web_app
    python manage.py migrate 

5. Run the Server
    ```bash
    python manage.py runserver
