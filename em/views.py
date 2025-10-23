from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        subject='SMTP Test from Django',
        message='This is a test email from your Django app.',
        from_email=None,  
        recipient_list=['your_email@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Test email sent successfully!")

