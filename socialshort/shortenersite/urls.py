from django.conf.urls import patterns, url

urlpatterns = patterns('shortenersite.views',
                       url(r'^$', 'index', name='home'),
                       # for our home/index page

                       url(r'^(?P<short_id>\w{6})/s$',
                           'redirectStats', name='redirectStats'),

                       url(r'^(?P<short_id>\w{6})$',
                           'redirectOriginal', name='redirectOriginal'),
                       # when short URL is requested it redirects to original
                       # URL

                       url(r'^url$', 'shortenUrl', name='shortenUrl'),
                       # this will create a URL's short id and return the short
                       # URL
                       )
