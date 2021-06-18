from django.conf.urls import patterns
from django.conf.urls import url

from mailing_lists.views import MailingListsListAllView


urlpatterns = patterns(
    '',
    url(r'^$', MailingListsListAllView.as_view(), name='list'),
)
