Steps to Generate an App-Specific Password:

## Enable 2-Step Verification:

Go to your Google Account.
Navigate to Security > 2-Step Verification and enable it if it’s not already turned on.

## Generate App-Specific Password:

Once 2-Step Verification is enabled, go to Security > App Passwords.
In the App Passwords section, choose Mail as the app and your device (e.g., Computer) as the device type.
Google will generate a 16-character app password. Copy this password.

## Update Your Script:

In your Python script, use the generated 16-character password in place of your usual email password in the email_password variable.
Once you’ve updated your password with the app-specific one, the email sending should work without errors.

For more information, you can refer to the official Google support page.
