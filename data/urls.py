"""data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio.views import index,FeedbackView, BotUserView,AboutMeVIew,BlogView,PortfolioView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('api/v/bot-user/',BotUserView.as_view(),name='bot-users'),
    path('api/v/feedbacks/', FeedbackView.as_view(), name='feedbacks'),
    path('api/v/about-me/', AboutMeVIew.as_view()),
    path('api/v/blog/', BlogView.as_view()),
    path('api/v/portfolio/', PortfolioView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
