from django.urls import path
from . import views
app_name = 'newsapp'
urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('business_news', views.business_news, name='business_news'),
    path('sports_news', views.sports_news, name='sports_news'),
    path('tech_news', views.tech_news, name='tech_news'),
    path('entertainment_news', views.entertainment_news, name='entertainment_news'),
    path('health_news', views.health_news, name='health_news'),
    path('science_news', views.science_news, name='science_news'),
    path('international_news', views.international_news, name='international_news'),

]
