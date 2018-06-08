from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    re_path(r'^$', api_root),
    re_path(r'^snippets/$', snippet_list, name='snippet-list'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    re_path(r'^users/$', user_list, name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
