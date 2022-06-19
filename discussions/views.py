from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Discussion
from .forms import DiscussionCreateForm


class UserDiscussionsListView(ListView):
    model = Discussion
    template_name = 'discussion/user_discussion.html'

    # context_object_name = 'blog_post_user_list'  # Представление_модель_что это
    # queryset = Post.objects.filter(author=2).order_by('-date_created')
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created')
    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['blog_post_user_list'] = queryset.order_by('-date_created')
        return context


# class DiscussionCreateView(LoginRequiredMixin, CreateView):
#     model = Discussion
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussion/user_detail_discussion.html'
    context_object_name = 'blog_post_detail'


@login_required
def discussion_create(request):
    if request.method == 'POST':
        form = DiscussionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            new_discussion = form.save(commit=False)  # Открывается в ОЗУ
            new_discussion.author = request.user
            new_discussion.save()
            messages.success(request, 'Дискуссия добавлена')
            return redirect(new_discussion.get_absolute_url())

    else:
        form = DiscussionCreateForm()

    return render(request, 'discussion/create_form.html', {'form': form})
