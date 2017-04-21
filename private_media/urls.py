from django.conf.urls import url
from django.conf import settings
from private_media.views import serve_private_fileRest, serve_private_file


urlpatterns = [

]
#condition for validation of RESTFRAMEWORK
if hasattr(settings,'PRIVATE_REST_FRAMEWORK_AUTH'):
	if settings.PRIVATE_REST_FRAMEWORK_AUTH:
		
		additional_settings  += [
			url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')), views.serve_private_fileRest,),
		]
	else:
		additional_settings += ['private_media.views',
			url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')), serve_private_file,),
		] 
else:
    additional_settings += ['private_media.views',
    	url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')),serve_private_file,),
	]


urlpatterns += additional_settings