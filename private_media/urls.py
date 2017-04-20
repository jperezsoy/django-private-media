from django.conf.urls import url
from django.conf import settings


urlpatterns = [

]
#condition for validation of RESTFRAMEWORK
if hasattr(settings,'PRIVATE_REST_FRAMEWORK_AUTH'):
	if settings.PRIVATE_REST_FRAMEWORK_AUTH:
		from private_media import views
		additional_settings  += ['private_media.views',
			url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')), views.serve_private_fileRest.as_view()),
		]
	else:
		additional_settings += ['private_media.views',
			url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')), 'serve_private_file',),
		] 
else:
    additional_settings += ['private_media.views',
    	url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')), 'serve_private_file',),
	]


urlpatterns += additional_settings