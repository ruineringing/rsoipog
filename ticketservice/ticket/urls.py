from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ticket import views

urlpatterns = [
    url(r'^ticket/$', views.TicketList.as_view(), name='ticket-list'),
    url(r'^ticket/(?P<pk>[0-9]+)/$', views.TicketDetail.as_view(), name='ticket-detail'),
]