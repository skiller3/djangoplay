from django.conf.urls import patterns, url
from constraints import views

urlpatterns = patterns("",
                        url(r'^$', views.index, name="index")
                        )
