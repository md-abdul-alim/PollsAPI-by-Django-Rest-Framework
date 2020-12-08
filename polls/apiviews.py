from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer


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
