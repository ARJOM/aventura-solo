from django.urls import path

from . import views as steps

app_name = 'solo'

urlpatterns = [
    # Steps
    path('step/<pk>', steps.StepDetailView.as_view(), name='step-detail'),
    path('', steps.StartTemplateView.as_view(), name='home')
]
