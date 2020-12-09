from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from .views import polls_detail, polls_list
from .apiviews import ApiPollList, ApiPollDetail, ApiChoiceList, ApiCreateVote, ApiPollDetail, PollViewSet, UserCreate, LoginView

schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
# Alternative of apipolls & apipolls/<int:pk>/ url
router.register('PollViewSet', PollViewSet, basename='polls')

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user'),
    # login/ & loginn both direct browser url may not work. this will work good in postman POST method
    path('login/', LoginView.as_view(), name='login'),
    #path('loginn/', views.obtain_auth_token, name="login"),

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

    path('swagger-docs/', schema_view),
    path('docs', include_docs_urls(title='Polls API')),
]
urlpatterns += router.urls
