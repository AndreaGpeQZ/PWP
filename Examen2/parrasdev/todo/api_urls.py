from django.urls import path
from . import api_views

urlpatterns = [
    path('ids/', api_views.ids_list, name='api_ids'),
    path('ids-titles/', api_views.ids_titles_list, name='api_ids_titles'),
    path('unresolved-titles/', api_views.unresolved_titles_list, name='api_unresolved_titles'),
    path('resolved-titles/', api_views.resolved_titles_list, name='api_resolved_titles'),
    path('ids-userid/', api_views.ids_userid_list, name='api_ids_userid'),
    path('resolved-userid/', api_views.resolved_userid_list, name='api_resolved_userid'),
    path('unresolved-userid/', api_views.unresolved_userid_list, name='api_unresolved_userid'),
]
