from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trend_10/', views.all_trend_10, name='all_trend_10'),
    path('trend_month/', views.all_trend_a_month, name='all_trend_a_month'),
    path('news/detail/<int:pk>/', views.DetailNews.as_view(), name='DetailNews'),
    path('search/', views.search, name='search'),
    path('news/<int:pk>/comment/', views.comment_add, name='comment_add'),
]

