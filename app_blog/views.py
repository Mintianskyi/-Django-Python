# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Category

class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(main_page=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ArticleCategory(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context