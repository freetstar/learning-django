from django.conf.urls.defaults import *
from items.models import Item,Photo
from django.views.generic import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^gallery/', include('gallery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic',
            url(r'^$','simple.direct_to_template',
                kwargs={
                    'template': 'index.html',
                    'extra_context': {'item_list': lambda: Item.objects.all()}
            },
            name='index'
        ),
            url(r'^items/$', 'list_detail.object_list',
                kwargs={
                    'queryset': Item.objects.all(),
                    'template_name': 'items_list.html',
                'allow_empty': True
            },
            name='item_list'
        ),
            url(r'^items/(?P<object_id>\d+)/$', 'list_detail.object_detail',
                kwargs={
                    'queryset': Item.objects.all(),
                    'template_name': 'items_detail.html'
                },
            name='item_detail'
        ),
            url(r'^photos/(?P<object_id>\d+)/$', 'list_detail.object_detail',
                kwargs={
                    'queryset': Photo.objects.all(),
                    'template_name': 'photos_detail.html'
                },
            name='photo_detail'
        ),
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
           ),            
    )
