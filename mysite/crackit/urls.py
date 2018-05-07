from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url('game', views.start, name='start'),
	url('help', views.help, name='help'),
	url('end', views.end, name='end'),
	url('level2', views.start1, name='start1'),
	url('level3', views.start2, name='start2'),
	url('level4', views.start3, name='start3'),
	url('level5', views.start4, name='start4'),
	url('level6', views.start5, name='start5'),
	url('level7', views.start6, name='start6'),
	url('level8', views.start7, name='start7'),
	url('level9', views.start8, name='start8'),
	url('level10', views.start9, name='start9'),
	url('level11', views.start10, name='start10'),
        url('level12', views.start11, name='start11'),
	url('level13', views.start12, name='start12'),
	url('level14', views.start13, name='start13'),
	url('level15', views.start14, name='start14')]
