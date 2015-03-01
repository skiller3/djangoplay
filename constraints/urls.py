from django.conf.urls import patterns, url
from constraints import views

urlpatterns = patterns("",
    url(r'^update_asset/(?P<symbol>[a-zA-Z0-9]+)$', views.update_asset, name="update_asset"),
    url(r'^(?P<symbol>[a-zA-Z0-9]+)$', views.asset_detail, name="asset_details"),
    url(r'^$', views.index, name="index")
)
