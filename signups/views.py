from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
from .forms import SignUpForm
def home(request):


    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))

def thankyou(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, "Thank you for joining!")
        subject = "Thank you for subscribed to us!"
        message = "Thank you for subscribed to us!\nWe are glad to see you among our customers!"
        from_message = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_message, to_list)
        return HttpResponseRedirect("/thank-you/")

    return render_to_response("thankyou.html", locals(), context_instance=RequestContext(request))

def aboutus(request):

    return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))

