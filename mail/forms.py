from django import forms
from django.forms import TextInput, Textarea, EmailInput, ClearableFileInput, CheckboxInput

from .models import Email, Sort


class ContactForm(forms.ModelForm):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Theme', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)

    # attach = forms.FileField(label='Attachment', widget=forms.ClearableFileInput, required=False)

    class Meta:
        model = Email
        fields = ["from_email", "subject", "message"]  # <- "attach"
        widgets = {"from_email": EmailInput(attrs={'class': 'form-control', 'placeholder': 'Полчучатель'}),
                   "subject": TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема'}),
                   "message": Textarea(attrs={'class': 'form-control', 'placeholder': 'Сообщение'})
                   # "attach": ClearableFileInput(
                   #    attrs={'class': 'form-control', 'placeholder': 'Вложение', 'multiple': True})
                   }


class SortForm(forms.ModelForm):
    status = forms.BooleanField(label='status', required=True)
    class Meta:
        model = Sort
        fields = ["status"]
    #    widgets = {
  #          "status": CheckboxInput(attrs={'class': 'form-check', 'name': 'choice', 'value': {"new", "old", "subject"}})
    #               }
