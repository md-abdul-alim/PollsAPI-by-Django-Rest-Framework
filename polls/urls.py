from django.urls import path
from .views import polls_detail, polls_list
from .apiviews import ApiPollList, ApiPollDetail

urlpatterns = [
    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:pk>/', polls_detail, name='polls_detail'),
    path('apipolls/', ApiPollList.as_view(), name='ApiPollList'),
    path('apipolls/<int:pk>/', ApiPollDetail.as_view(), name='ApiPollDetail'),
]
