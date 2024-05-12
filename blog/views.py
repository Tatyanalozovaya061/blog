import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from blog.models import Blog
from users.models import User


class BlogCreateView(CreateView):
    """ Cоздание блога """
    model = Blog
    fields = ('title', 'content', 'image', 'is_subscription', 'date_created',)
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        """ Присваивание id """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class BlogListView(ListView):
    """ Список блогов"""
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    """ Детальное рассмотрение блога """
    model = Blog
    template_name = 'blog/blog_detail.html'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """ Изменение блога """
    model = Blog
    fields = ('title', 'content', 'image',)
    template_name = 'blog/blog_update.html'
    success_url = reverse_lazy('blog:home')

    def get_object(self, queryset=None):
        """ Обновлять блог может только автор """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление блога """
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_object(self, queryset=None):
        """ Удалить блог может только автор """

        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class HomeView(TemplateView):
    """ Домашняя страница """
    template_name = 'blog/home.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Blog.objects.all()
        context_data['publish_blog_count'] = len(Blog.objects.filter(is_published=True))
        context_data['users_count'] = len(User.objects.all())

        return context_data
