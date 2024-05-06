from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    """ Cоздание блога """
    model = Blog
    fields = ('title', 'content', 'image', 'is_subscription',)
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog_list')

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
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog_list')

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
