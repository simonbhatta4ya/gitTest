"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#from polls.views import home_view, about_view, contact_view, ContactView, ContactTemplateView
#from polls.views import HomeView, AboutView, ContactView

from polls.views import HomeView

# polls.views > > > LN : 41 to 83

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', home_view, name='home'),
#     url(r'^about/$', about_view, name='about'),
#     url(r'^contact/$', contact_view, name='contact'),
#     url(r'^contact-me/$', ContactView.as_view()),
#     url(r'^contact-me/(?P<id>\d+)/$', ContactView.as_view()),
#     url(r'^contact-me-too/$', ContactTemplateView.as_view()),
# ]

from django.views.generic import TemplateView

from polls.views import restaurant_listview, RestaurantListView, RestaurantDetailView #SearchRestaurantListView #MexicanRestaurantListView, AsianFusionRestaurantListView, 


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     #url(r'^$', HomeView.as_view()),
#     url(r'^$', TemplateView.as_view(template_name='home.html')),
#     #url(r'^restaurants/$', restaurant_listview),
#     url(r'^restaurants/$', RestaurantListView.as_view()),
#     #url(r'^restaurants/mexican/$', MexicanRestaurantListView.as_view()),
#     #url(r'^restaurants/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),
#     url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
#     #url(r'^restaurants/asian/$', AsianFusionRestaurantListView.as_view()),
#     #
#     url(r'^restaurants/(?P<pk>\w+)/$', RestaurantDetailView.as_view()),
#     #url(r'^about/$', AboutView.as_view()),
#     url(r'^about/$', TemplateView.as_view(template_name='about.html')),
#     #url(r'^contact/$', ContactView.as_view()),
#     url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
# ]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    ###url(r'^restaurants/(?P<pk>\w+)/$', RestaurantDetailView.as_view()),
    url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]
