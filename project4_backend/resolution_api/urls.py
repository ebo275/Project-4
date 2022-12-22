from django.urls import path
from . import views

urlpatterns = [
    path('api/resolutions', views.ResolutionList.as_view(), name='resolution_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/resolutions/<int:pk>', views.ResolutionDetail.as_view(), name='resolution_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
