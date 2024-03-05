from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.views.generic import DetailView

from .models import News, Comment
from .forms import CommentForm


def view_news(request, news_id):
    news = News.objects.get(id=news_id)
    news.viewers += 1
    news.save()
    return render(request, 'posts/detail.html', {'news': news})


def home(request):
    trend_10 = News.objects.filter(post_date__gte=datetime.now().date() - timedelta(days=10)).order_by('-viewers')[:6]
    end_date_month = datetime.now().date()
    start_date_month = end_date_month - timedelta(days=30)
    trend_month = News.objects.filter(post_date__gte=start_date_month, post_date__lte=end_date_month).order_by('-viewers')[:6]
    return render(request, 'posts/index.html', context={'trend_10': trend_10, 'trend_month': trend_month})


def all_trend_10(request):
    trend_10 = News.objects.filter(post_date__gte=datetime.now().date() - timedelta(days=10)).order_by('-viewers')
    return render(request, 'posts/trend_10.html', context={'trend_10': trend_10})


def all_trend_a_month(request):
    end_date_month = datetime.now().date()
    start_date_month = end_date_month - timedelta(days=30)
    trend_month = News.objects.filter(post_date__gte=start_date_month, post_date__lte=end_date_month).order_by('-viewers')
    return render(request, 'posts/trend_month.html', context={'trend_month': trend_month})


class DetailNews(DetailView):
    model = News
    template_name = 'posts/detail.html'
    context_object_name = 'content'

    def get(self, request, *args, **kwargs):
        news = self.get_object()
        viewed_news = request.session.get('viewed_news', [])
        if news.pk not in viewed_news:
            news.viewers += 1
            news.save()
            viewed_news.append(news.pk)
            request.session['viewed_news'] = viewed_news
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comment_set.all()
        return context


@login_required(login_url='/login/')
def comment_add(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.news = news
            new_comment.save()
            return redirect('DetailNews', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'posts/comment_add.html', {'form': form, 'news': news})


def comment_det(request):
    comments = Comment.objects.all()
    return render(request, 'posts/detail.html', {'comments': comments})


def search(request):
    if request.method == 'POST':
        search_result = request.POST['searched']
        result = News.objects.filter(Q(title__icontains=search_result) | Q(content__icontains=search_result))
        return render(request, 'posts/search.html', {'news': result})
    else:
        return render(request, 'posts/search.html')


