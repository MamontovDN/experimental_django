from django.core.exceptions import PermissionDenied
from django.db.models import F, ExpressionWrapper, Q, BooleanField
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from posts.forms import PostForm
from posts.models import Post, Category


class IndexView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context

    def get_queryset(self):
        return self.model.objects.select_related('author', 'category')


class PostByCategory(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"
    extra_context = {"title": "Категория"}
    # 404 для пустого списка
    allow_empty = False

    def get_queryset(self):
        return get_object_or_404(Category, pk=self.kwargs[
            "category_id"]).posts.select_related('author', 'category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = (
                "Категория: "
                + get_object_or_404(Category,
                                    pk=self.kwargs["category_id"]).title
        )
        return context


class PostView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    context_object_name = "item"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = F("views") + 1
        obj.save()
        return super(PostView, self).get(self, request, *args, **kwargs)


class CreatePost(CreateView):
    form_class = PostForm
    template_name = "postForm.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        for field in form.errors:
            form[field].field.widget.attrs["class"] += " is-invalid"
        return super(CreatePost, self).form_invalid(form)


class PermissionMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if not obj.author == self.request.user:
            raise PermissionDenied()
        else:
            return obj


class DeletePost(PermissionMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "postForm.html"

    def get_context_data(self, **kwargs):
        return super(UpdatePost, self).get_context_data()


"""
# аналог на FBV
def index(request):
    num = request.GET.get("co", -1)
    posts = Post.objects.select_related("author", "category")
    return render(request, "index.html", {"posts": posts, "num": int(num)})


def category_posts(request, category_id):
    num = request.GET.get("co", -1)
    category = get_object_or_404(Category, pk=category_id)
    posts = category.posts.select_related("author")
    return render(request, "index.html", {"posts": posts, "num": num})


def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "index.html", {"posts": [post]})
"""
