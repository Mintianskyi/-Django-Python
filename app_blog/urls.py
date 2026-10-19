from django.urls import path
from .views import HomePageView, ArticleDetail, ArticleCategory

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/<slug:slug>/', ArticleCategory.as_view(), name='articles-category-list'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>/', ArticleDetail.as_view(), name='news-detail'),
]