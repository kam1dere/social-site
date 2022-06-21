from django import forms
import datetime


class ContactForm(forms.Form):
    date_created = forms.DateField(help_text='Заполнить сейчас')
    subject = forms.CharField(max_lenght=100)
    message = forms.CharField(max_lenght=500)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean_date_created(self):
        data = self.clean_date['date_created']
        if data < datetime.date.today():
            raise forms.ValidationError("Форма не действительна, перейдите на сайт прострочена дата")


