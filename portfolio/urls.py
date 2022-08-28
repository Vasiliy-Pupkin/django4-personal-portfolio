from django.urls import path
from . import views


urlpatterns = [
    path('about-text', views.about, name='about'),
    path('portfolio', views.view_portfolio, name='view_portfolio'),
]
