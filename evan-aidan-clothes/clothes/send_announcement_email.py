# yourapp/send_announcement_email.py
from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from yourapp.models import Subscriber  # or your User model

class Command(BaseCommand):
    help = "Send a one-off sale email to all subscribers"

    def handle(self, *args, **options):
        subject = "🔥 Big Sale This Weekend!"
        from_email = settings.DEFAULT_FROM_EMAIL

        text_content = "Don't miss out! Huge discounts available this weekend only."
        html_content = """
        <html>
          <body style="font-family: sans-serif; color: #333;">
            <h1>🔥 Big Sale This Weekend!</h1>
            <p>We’re giving up to <strong>50% off</strong> everything in our store.</p>
            <p><a href="https://yourdomain.com/shop" 
                  style="color:#fff;background:#e63946;padding:10px 20px;
                         text-decoration:none;border-radius:4px;">Shop Now</a></p>
            <hr>
            <small>You received this email because you signed up for updates.</small>
          </body>
        </html>
        """

        # Get your email list (from your subscriber table or users who opted in)
        recipients = list(
            Subscriber.objects.values_list("email", flat=True)
        )

        # Send individually (safer for large lists)
        for email in recipients:
            msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        self.stdout.write(self.style.SUCCESS(f"Sent announcement email to {len(recipients)} subscribers"))
