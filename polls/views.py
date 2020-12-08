from django.shortcuts import render, get_object_or_404
from .models import Poll, Choice, Vote
from django.http import JsonResponse
# Create your views here.

# API Type 1


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values(
        "question", "created_by__username", "pub_date"))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)

# Choosing the base class to use
# We have seen 4 ways to build API views until now
# •	Pure Django views
# •	APIView subclasses
# •	generics.* subclasses
# •	viewsets.ModelViewSet
# So which one should you use when? My rule of thumb is,
# •	Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
# •	Use generics.* when you only want to allow some operations on a model
# •	Use APIView when you want to completely customize the behaviour
