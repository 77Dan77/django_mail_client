from Myapp.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import ContactForm, SortForm
from django.conf import settings
from .models import Email, Sort


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)  # <- request.FILES
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            # attach = form.cleaned_data['attach']
            RECIPIENTS_EMAIL.append(from_email)
            form.save()
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL, fail_silently=False)
            # mail = EmailMessage(f'{subject} от {from_email}', message,
            #    DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            # mail.attach(attach.name, attach.read(), attach.content_type)
            # mail.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "mail/email.html", {'form': form})


def edit(request, id):
    try:
        form = Email.objects.get(id=id)

        if request.method == "POST":
            form.name = request.POST.get("name")
            form.age = request.POST.get("age")
            form.save()
            return redirect('success')
        else:
            return render(request, "mail/email.html", {'form': form})
    except Email.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, id):
    try:
        mail = Email.objects.get(id=id)
        mail.delete()
        return redirect('mail')
    except Email.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def sort(request):
    if request.method == "POST":
        form = SortForm(request.POST)
        form.save()
    else:
        pass
    return render(request, "mail/report.html")


def success_view(request):
    #check = Sort.objects.get("val")
    #if check == 'new':
    #    messages = Email.objects.order_by('-id')
    #elif check == 'old':
    #    messages = Email.objects.order_by('id')
    # else:
    #    messages = Email.objects.order_by('-subject')
    messages = Email.objects.order_by('-id')
    return render(request, 'mail/report.html', {'title': 'Success', 'messages': messages})


def index(request):
    return render(request, 'mail/after_sending.html')


def home(request):
    return render(request, 'mail/home.html')
