from django.views.generic import DetailView, TemplateView

from app.solo import models


class StepDetailView(DetailView):
    model = models.Step
    template_name = 'step/detail.html'


class StartTemplateView(TemplateView):
    template_name = 'step/home.html'
