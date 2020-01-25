from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
 

# Create your views here.
def contact_view(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "contact.html", {'form': form, 'submitted': submitted})
