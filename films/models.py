from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('films:film_list_by_category', args=[self.slug])



class Film(models.Model):
    category = models.ForeignKey(Category, related_name='films')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='posters', blank=True)
    youtube = models.CharField(max_length=300, default='')
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField()
    country = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    seasons = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering= ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('films:film_detail', args=[self.id, self.slug])

class Comment(models.Model):
    film = models.ForeignKey(Film, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Commented by {} on {}'.format(self.name, self.film)

class News(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added',)

    def __str__(self):
        words = self.body.split()
        countWords = int(len(words)/2)
        if countWords > 100:
            countWords = 100
        st = ''
        for i in range(countWords):
            st += words[i]
            st +=' '
        return st +'...'

    def get_absolute_url(self):
        return reverse('films:news_info', args=[self.slug])


class Actor(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    film = models.ManyToManyField(Film)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)
    filmSlug = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='actors', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name = 'actor'
        verbose_name_plural = 'actors'

    def __str__(self):
        words = self.description.split()
        countWords = int(len(words)/2)
        if countWords > 100:
            countWords = 100
        st = ''
        for i in range(countWords):
            st += words[i]
            st +=' '
        return st +'...'



    def get_absolute_url(self):
        return reverse('films:actor_info', args=[self.slug])
