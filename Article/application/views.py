from django.views.generic.list import ListView

from application.models import Article

class ArticleListView(ListView):

    model = Article