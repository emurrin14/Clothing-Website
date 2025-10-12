from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

# Welcome email
def send_welcome_email(user):
    subject = "Welcome to Our Platform 🎉"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]

    text_content = f"Hi {user.username}, welcome to our platform!"
    html_content = f"""
    <html>
      <body style="font-family: sans-serif; color: #333;">
        <h2>Welcome, {user.username}! 🎉</h2>
        <p>We’re excited to have you join us.</p>
        <p>You can now <a href='https://yourdomain.com/login'>log in</a> and get started.</p>
        <hr>
        <small>This email was sent automatically via MailerSend.</small>
      </body>
    </html>
    """

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# One-off sale email
def send_sale_email(subscribers):
    subject = "🔥 Big Sale This Weekend!"
    from_email = settings.DEFAULT_FROM_EMAIL
    text_content = "Don't miss out! Huge discounts this weekend."
    
    # Optional: use template
    html_content = render_to_string("emails/sale_email.html", {})

    for email in subscribers:
        msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
