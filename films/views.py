from django.shortcuts import render, get_object_or_404
from .models import Category, Film, Comment, News, Actor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm



def news_info(request, slug):
    one_news = get_object_or_404(News, slug=slug)
    return render(request, 'films/film/one_news.html', {'one_news': one_news})

def film_detail(request, id, slug):
    film = get_object_or_404(Film, id=id, slug=slug)
    comments = film.comments.filter(active=True)
    actors = Actor.objects.filter(filmSlug=slug)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.film = film
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'films/film/detail.html',{'film': film,
                                                     'comments': comments,
                                                     'comment_form': comment_form,
                                                     'actors': actors})

def film_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    news = News.objects.all()[:3]
    films = Film.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        films = films.filter(category=category)

    paginator = Paginator(films, 4)
    page = request.GET.get('page')
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        films = paginator.page(1)
    except EmptyPage:
        films = paginator.page(paginator.num_pages)
    return render(request, 'films/film/list.html', {'page': page,
                                                    'category': category,
                                                    'news': news,
                                                    'categories': categories,
                                                    'films': films})

def show_all_news(request):
    All_news = News.objects.all()
    paginator = Paginator(All_news, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'films/film/news.html', {'page': page,
                                                        'posts': posts})

def actors_list(request):
    actors = Actor.objects.all()
    paginator = Paginator(actors, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'films/film/actors_list.html', {'page': page,
                                                            'posts': posts})

def actor_info(request, slug):
    actor = get_object_or_404(Actor, slug=slug)
    return render(request, 'films/film/actor.html', {'actor': actor})
