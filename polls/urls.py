from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import polls_detail, polls_list
from .apiviews import ApiPollList, ApiPollDetail, ApiChoiceList, ApiCreateVote, ApiPollDetail, PollViewSet, UserCreate

router = DefaultRouter()
# Alternative of apipolls & apipolls/<int:pk>/ url
router.register('PollViewSet', PollViewSet, basename='polls')

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user'),

    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:pk>/', polls_detail, name='polls_detail'),
    # API urls
    path('apipolls/', ApiPollList.as_view(), name='ApiPollList'),
    path('apipolls/<int:pk>/', ApiPollDetail.as_view(), name='ApiPollDetail'),
    # Alternative of apipolls & apipolls/<int:pk>/ url


    path("polls/<int:pk>/choices/", ApiChoiceList.as_view(), name='ApiChoiceList'),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         ApiCreateVote.as_view(), name='ApiCreateVote'),
    # for test api
    # path('apichoices/', ApiChoiceList.as_view(), name='ApiChoiceList'),
    # path('apivote/', ApiCreateVote.as_view(), name='ApiCreateVote'),
]
urlpatterns += router.urls
