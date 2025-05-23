import smtplib
from email.message import EmailMessage

def send_email_alert(subject, body, to_email):
    # Replace with your email credentials
    sender_email = "lakshmipriya292004@gmail.com"
    sender_password = "imsq jven tytk rkqx"  # Use an app-specific password if 2FA is enabled

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("✅ Email alert sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
