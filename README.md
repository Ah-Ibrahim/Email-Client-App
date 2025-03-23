# Email Client Application

## Overview

This project consists of a simple Python-based email client application that allows users to send and receive emails using **SMTP (smtplib)** and **IMAP (imaplib)**. The script is designed to work with **Gmail**, but can be adjusted for other email providers.

## Features

-   **Send Emails** using SMTP.
-   **Receive Emails** from any folder using IMAP.
-   **Fetch all emails** from the "inbox".
-   **Error Handling** to manage connection failures and authentication issues.

## Requirements

Ensure you have the following installed:

-   Python 3.x
-   Required libraries:
    ```sh
    pip install smtplib imaplib email
    ```

## Setup Instructions

### 1. Enable Gmail Access

Since Google restricts third-party access, you need to:

-   Enable **2-Step Verification** in your Google Account.
-   Generate an **App Password** from [Google's App Passwords page](https://myaccount.google.com/apppasswords).

### 2. Update Credentials

Replace the placeholders in the script with your Gmail credentials and recipient email.

## Usage

### Sending Email

Run `sender.py` with your credentials and recipient details:

```python
send_email(
    "sender@gmail.com",
    "sender_app_password",
    "receiver@example.com",
    "Subject Here",
    "Email Body Here"
)
```

### Receiving Emails

Run `receiver.py` to fetch last emails:

```python
receive_email("receiver@gmail.com", "receiver_app_password")
```

## Notes

-   This script is configured for **Gmail**. To use another provider, update the **SMTP and IMAP server settings**.
-   Do not use your personal password. Always use an **App Password** for security.
-   You may need to adjust the `mail.select("inbox")` line if using another email provider.
-   If sent email was not being fetched, go to your gmail and make sure you marked it as unspam.

## License

This project is open-source and can be modified for educational purposes.
