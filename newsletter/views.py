from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

from .models import NewsUsers
from .forms import NewsUserForm

# Create your views here.
def newsletter_subscribe_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            instance = form.save(commit=False)
            if NewsUsers.objects.filter(email=instance.email).exists():
                print("Your email already exists in our database!")
            else:
                instance.save()
                send_mail('Simple blog subscription confirmation', f'You\'ve successfully subscribed to our newsletter service. Click the following link to visit our site. {request.get_host()}', '95mainuddin@gmail.com', [instance.email,], fail_silently=False)
                print("Your email has been submitted to our database")

    return HttpResponseRedirect(reverse('home'))