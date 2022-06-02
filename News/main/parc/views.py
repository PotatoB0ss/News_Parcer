
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import News
from .scrap import scrap



class Base(ListView):
    model = News
    template_name = 'parc/base.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categs'] = set(News.objects.values_list('categ', flat=True))
        return context


class Rubric(ListView):
    model = News
    template_name = 'parc/rubric.html'
    context_object_name = 'current'
    paginate_by = 5

    def get_queryset(self):
        return News.objects.filter(categ=self.kwargs['sstr'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categs'] = set(News.objects.values_list('categ', flat=True))
        return context


class Search(ListView):

    template_name = 'parc/base.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def f_scrap(request):
    scrap()
    return HttpResponseRedirect('/admin/parc/news/')


