from .views import IndexView, AboutView, UserView
from django.urls import path

urlpatterns = [
    path(route='', view=IndexView.as_view(), name='index'),
    path(route='hakkimizda/', view=AboutView.as_view(), name='about'),
    path(route='yolcu/', view=UserView.as_view(), name='user')
]
