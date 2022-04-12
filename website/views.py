from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'website/home.html', {})


def about(request):
    return render(request, 'website/about.html', {})


def courses(request):
    return render(request, 'website/courses.html', {})


def contact(request):
    return render(request, 'website/contact.html', {})


def message(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message_ = request.POST['message']

        infos = 'Nom: ' + message_name + ',  Email: ' + message_email + ',  Téléphone: ' + message_phone + ',  Message: ' + message_

        # Send an email
        send_mail(
            'Nouveau message de ' + message_name,
            infos,
            message_email,
            ['labofarid22@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'website/message.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'message': message,
        })

    else:
        return render(request, 'website/home.html', {})
