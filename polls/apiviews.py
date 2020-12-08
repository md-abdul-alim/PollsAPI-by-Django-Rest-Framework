from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets

# queryset: This determines the initial queryset. The queryset can be further filtered, sliced or ordered by the view.
# serializer_class: This will be used for validating and deserializing the input and for serializing the output.


# ListCreateAPIView: Get a list of entities, or create them. Allows GET and POST.
# API Type 3
class ApiPollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

# RetrieveDestroyAPIView: Retrieve an individual entity details, or delete the entity. Allows GET and DELETE.

# API Type 3


class ApiPollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
# PollViewSet is Alternative of ApiPollList & ApiPollDetail
# API Type 4


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

# API Type 3


class ApiChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer
# for test
# class ApiChoiceList(generics.ListCreateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

# CreateAPIView: Allows creating entities, but not listing them. Allows POST.

# API Type 2


class ApiCreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for test
# class ApiCreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


"""
##Manual API by pure Django
class ApiPollList(APIView):
    def get(self, request):
        MAX_OBJECTS = 20
        polls = Poll.objects.all()[:MAX_OBJECTS]
        data = PollSerializer(polls, many=True).data
        return Response(data)


class ApiPollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)
"""
