from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
class Intro(View):
    template_name = 'intro.html'

    def get(self, request):
        return render(request, self.template_name)