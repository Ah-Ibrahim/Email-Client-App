## receive_email.py
import imaplib
import email


def receive_email(email_user, email_password):
    try:
        # Connect to the IMAP server
        imap_server = "imap.gmail.com"  # Change based on your email provider
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_user, email_password)
        mail.select("inbox")

        # Search for the latest email
        status, messages = mail.search(None, "ALL")
        mail_ids = messages[0].split()
        latest_email_id = mail_ids[-1]  # Get the latest email

        # Fetch the latest email
        status, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]

        # Parse email content
        msg = email.message_from_bytes(raw_email)
        email_from = msg["From"]
        email_subject = msg["Subject"]

        # Extract email body
        email_body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    email_body = part.get_payload(decode=True).decode()
                    break
        else:
            email_body = msg.get_payload(decode=True).decode()

        print(f"From: {email_from}\nSubject: {email_subject}\nBody:\n{email_body}")

        mail.logout()
    except Exception as e:
        print(f"Error receiving email: {e}")


receive_email("your_email@gmail.com", "receiver_app_password")
