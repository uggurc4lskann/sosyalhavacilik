from django.views import View
from django.shortcuts import render
from ..models import OurPurpose, About

class AboutView(View):
    def get(self, request, *args, **kwargs):
        __about = About.objects.all()

        return render(
            request=request,
            template_name='about.html',
            context={
                
                'about':__about
            }
        )