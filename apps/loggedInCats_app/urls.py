from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addNewCatPage$', views.addNewCatPage),
    url(r'^addNewCat$', views.addNewCat),
    url(r'^delete$', views.deleteCat),
    url(r'^editPage$', views.editCat),
    url(r'^edit$', views.edit),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^addLike$', views.addLike),
    url(r'^catsPage$', views.catsPage),

]