from django.shortcuts import render
from django.views import View
from .models import Education

class Index(View):
    context={}
    def get(self, request):
        self.context['education']=Education.objects.all()
        return render(request, 'portfolio/index.html', self.context)
    
    