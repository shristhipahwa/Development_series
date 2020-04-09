from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(label='Your Name', max_length=30,min_length=4)
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(label='Subject', max_length=100,min_length=4)
    message = forms.CharField(label='Message', widget=forms.Textarea)

