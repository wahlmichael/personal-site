from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Portfolio
from .forms import EmailForm
from django.core.mail import send_mail

def index(request): 
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['your_name'])
            message_to_send = 'Message from {} at email {}: {}'.format(
                form.cleaned_data['your_name'],
                form.cleaned_data['your_email'],
                form.cleaned_data['your_message']
            )
            send_mail('message from website',
                    message_to_send,
                    'michaelwahldev@gmail.com',
                    ['michaelwahl9@gmail.com'])
            print(message_to_send)
            return HttpResponseRedirect("/")
    else:
        form = EmailForm()

    projects = Portfolio.objects.all()
    context = {
        'form': form,
        'projects': projects
    }
    return render(request, 'pages/index.html', context)