from django.views import View
from django.shortcuts import render
from ..models import OurPurpose, About

class IndexView(View):
    def get(self, request, *args, **kwargs):
        __purpose = OurPurpose.objects.all()
        __about = About.objects.all()


        return render(
            request=request,
            template_name='index.html',
            context={
                'purpose':__purpose,
                'about':__about
            }
        )