from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from home.urls import site_import_urls, api_urls
from search import views as search_views

from pybb.views import ProfileEditView
from home.views import Search, MovePostView, AorAddPostView, AorEditPostView, AorTopicView, move_post_processing
from home.forms import AORProfileForm, RegistrationFormCaptcha
from profiles.views import UserTopics, UserPosts, safe_logout
from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^registration/', include('registration.backends.hmac.urls')),
    url(r'^social/', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^import/', include(site_import_urls)),
    url(r'^api/', include(api_urls)),

    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormCaptcha),
        name="registration_register"),
    url(r'^accounts/logout/$', safe_logout, name='auth_logout'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^forum/profile/edit/$', ProfileEditView.as_view(form_class=AORProfileForm), name='pybb:edit_profile'),
    url(r'^forum/users/(?P<username>[^/]+)/topics/$', UserTopics.as_view(),
        name='user_topics'),
    url(r'^forum/users/(?P<username>[^/]+)/posts/$', UserPosts.as_view(),
        name='user_posts'),

    url(r'^forum/topic/(?P<pk>\d+)/$', AorTopicView.as_view(), name='topic'),
    url(r'^forum/topic/(?P<pk>\d+)/move/$', MovePostView.as_view(), name='move_post'),
    url(r'^forum/forum/(?P<forum_id>\d+)/topic/add/$', AorAddPostView.as_view(), name='add_topic'),
    url(r'^forum/topic/(?P<topic_id>\d+)/post/add/$', AorAddPostView.as_view(), name='add_post'),
    url(r'^forum/post/(?P<pk>\d+)/edit/$', AorEditPostView.as_view(), name='edit_post'),
    url(r'^forum/post/move/processing/$', move_post_processing, name='move_post_processing'),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),

    url(r'^messages/', include('forum_messages.urls')),

    url(r'^', include('social_django.urls', namespace='social')),
    url(r'^', include(wagtail_urls)),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
