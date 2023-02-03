from django.urls import path
from django.views.decorators.cache import cache_page

from .views import BookListView, BookDetailView, SearchResultsListView

urlpatterns = [
    path('', cache_page(60 * 5)(BookListView.as_view()), name='book_list'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail')
]
