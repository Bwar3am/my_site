from allauth.account.views import PasswordResetView
from django.conf import settings
from django.dispatch import receiver
from django.http import HttpRequest
from django.middleware.csrf import get_token

@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def send_reset_password_email(sender, instance, created, **kwargs):
    if created:
        # Create a post request to pass to the view
        request = HttpRequest()
        request.method = 'POST'

        # Set the absolute URL to be included in the email
        if settings.DEBUG:
            request.META['HTTP_HOST'] = '127.0.0.1:8000'
        else:
            request.META['HTTP_HOST'] = 'www.mysite.com'

        # Pass the post form data
        request.POST = {
            'email': instance.email,
            'csrfmiddlewaretoken': get_token(HttpRequest())
        }

        # Trigger the password reset view (email will be sent)
        PasswordResetView.as_view()(request)