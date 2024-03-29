from django.conf.urls import url
from django.conf import settings


from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(\d+)/$',views.image,name ='image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/(?P<category>\w+)', views.get_category_images,name='get_category_images'),
    url(r'^location/(?P<location>\w+)', views.get_images_by_location, name='get_images_by_location'),
   
]
