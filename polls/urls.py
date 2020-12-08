from django.urls import path
from .views import polls_detail, polls_list
from .apiviews import ApiPollList, ApiPollDetail, ApiChoiceList, ApiCreateVote

urlpatterns = [
    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:pk>/', polls_detail, name='polls_detail'),
    # API urls
    path('apipolls/', ApiPollList.as_view(), name='ApiPollList'),
    path('apipolls/<int:pk>/', ApiPollDetail.as_view(), name='ApiPollDetail'),

    path("polls/<int:pk>/choices/", ApiChoiceList.as_view(), name='ApiChoiceList'),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         ApiCreateVote.as_view(), name='ApiCreateVote'),
    # for test api
    # path('apichoices/', ApiChoiceList.as_view(), name='ApiChoiceList'),
    # path('apivote/', ApiCreateVote.as_view(), name='ApiCreateVote'),
]
