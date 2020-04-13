from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, get_connection
from django.contrib import messages
import os

def home(request):
    # submitted = False
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(

                cd['subject'],
                cd['yourname']+ "\n" +cd['message'],
                cd['email'],
                [os.environ.get('EMAIL_USER')],

                connection=con
                )

            messages.success(request, f'Message Sent ThankYou!')
            return redirect('home-page')

    else:
        form = ContactForm()

    return render(request, "Me/ME.html", {'form':form})
