from django.views import View
from django.shortcuts import render
from ..models import Title, UserInfo

class UserView(View):
    def get(self, request, *args, **kwargs):
        title = Title.objects.all()

        return render(
            request=request,
            template_name='user.html',
            context={
                'title':title,
                
            }
        )