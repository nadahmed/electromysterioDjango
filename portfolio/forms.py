from django import forms

class ContactForm(forms.Form):
    sender = forms.CharField(required=True, max_length=100)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length= 200)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=1000)