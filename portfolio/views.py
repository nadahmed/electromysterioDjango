from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Education, Work, Software, Hardware, Others
from .forms import ContactForm
from django.core.mail import send_mail

class Index(View):
    context={}
    def get(self, request):
        self.context['form'] = ContactForm()
        self.context['education']=Education.objects.all()
        self.context['works']=Work.objects.all()
        self.context['hardwares']=Hardware.objects.all()
        self.context['softwares']=Software.objects.all()
        self.context['others']=Others.objects.all()
        return render(request, 'portfolio/index.html', self.context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
#                print(subject,message,from_email,['nooraldinahmed@gmail.com'])
                send_mail(subject, message, from_email,['contact@electromysterio.tech'])
            except:
                return HttpResponse("Oops! Something's not right!")
            #return redirect('success')
            else:
                return HttpResponse('OK')
