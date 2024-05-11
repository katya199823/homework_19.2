from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Category, Blog


class HomeListView(ListView):
    model = Product


class ContactDetailView(DetailView):
    model = Product


class GameDetailView(DetailView):
    model = Product


class GameCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'photo', 'price_of_product', 'category')
    success_url = reverse_lazy('catalog:games_list')


class GameUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'photo', 'price_of_product')
    success_url = reverse_lazy('catalog:games_list')



class GameDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:games_list')


class GenresListView(ListView):
    model = Category


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    slug_field = 'slug'
    fields = ['title', 'description', 'photo']
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    slug_field = 'slug'
    fields = ['title', 'description', 'photo']

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
