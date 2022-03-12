from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    article_dict = {}
    for article in articles:
        article_dict[article] = {
            'title': article.title,
            'text': article.text,
            'published_at': article.published_at,
            'image': article.image
        }
    context = {'object_list': article_dict}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
