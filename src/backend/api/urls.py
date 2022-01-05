from django.urls import path, include
from rest_framework import routers

from api.views import login, policyViews, serverPreferencesViews, pluginPreferencesViews, familySelectionViews, individualPluginSelectionViews, reportViews, reportHostViews, hostPropertiesViews, reportItemViews, reportItemPropertiesViews, fileUploadView, fileHashesViews, wipeAppData


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', login),
    path('policy/', policyViews),
    path('policy/<int:id>', policyViews),
    path('server-preferences/', serverPreferencesViews),
    path('server-preferences/<int:id>', serverPreferencesViews),
    path('plugin-preferences/', pluginPreferencesViews),
    path('plugin-preferences/<int:id>', pluginPreferencesViews),
    path('family-selection/', familySelectionViews),
    path('family-selection/<int:id>', familySelectionViews),
    path('individual-plugin-selection/', individualPluginSelectionViews),
    path('individual-plugin-selection/<int:id>', individualPluginSelectionViews),
    path('report/', reportViews),
    path('report/<int:id>', reportViews),
    path('report-host/', reportHostViews),
    path('report-host/<int:id>', reportHostViews),
    path('host-properties/', hostPropertiesViews),
    path('host-properties/<int:id>', hostPropertiesViews),
    path('report-item/', reportItemViews),
    path('report-item/<int:id>', reportItemViews),
    path('report-item-properties/', reportItemPropertiesViews),
    path('report-item-properties/<int:id>', reportItemPropertiesViews),
    path('file-hashes/', fileHashesViews),
    path('single-file/', fileUploadView),
    path('delete-all/', wipeAppData),
    path('delete-all/<int:id>', wipeAppData)
]
